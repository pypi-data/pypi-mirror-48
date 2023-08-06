######################################################
# Author: Andrea Fioraldi <andreafioraldi@gmail.com> #
# License: BSD 2-Clause                              #
######################################################

from .context import get_debugger

import logging

l = logging.getLogger("angrdbg.got_builder")

#py2 and 3 support
try:
    xrange
    import itertools
    def range(start, stop, step):
        return iter(itertools.count(start, step).next, stop)
except NameError:
    pass

'''
def get_other_symbols_addrs(proj):
    i = 1
    while True:
        try:
            sym = proj.loader.main_object.get_symbol(i)
        except: break
        if sym.rebased_addr > 0:
            yield sym.name, sym.relative_addr
        i += 1
'''

def build_cle_got(proj, state):
    debugger = get_debugger()

    try:
        got_start, got_end = debugger.get_got()
    except BaseException:
        l.warning("cannot find .got.plt section, build_cle_got failed")
        return state

    entry_len = proj.arch.bits // 8

    got_start += 3 * entry_len  # skip first 3 entries

    empty_state = proj.factory.blank_state()
    state.memory.store(
        got_start,
        empty_state.memory.load(
            got_start,
            got_end -
            got_start))

    return state


def build_mixed_got(proj, state, concrete_imports=[]):
    debugger = get_debugger()

    try:
        got_start, got_end = debugger.get_got()
    except BaseException:
        l.warning("cannot find .got.plt section, build_mixed_got failed")
        return state
    
    try:
        plt_start, plt_end = debugger.get_plt()
    except BaseException:
        l.warning("cannot find .plt section, build_mixed_got failed")
        return state
    
    entry_len = proj.arch.bits // 8
    get_mem = debugger.get_dword if entry_len == 4 else debugger.get_qword

    got_start += 3 * entry_len  # skip first 3 entries

    empty_state = proj.factory.blank_state()

    for a in range(got_start, got_end, entry_len):
        state_val = empty_state.solver.eval(
            getattr(
                empty_state.mem[a],
                "uint%d_t" %
                proj.arch.bits).resolved)
        if state_val in proj._sim_procedures:
            if proj._sim_procedures[state_val].is_stub or proj._sim_procedures[state_val].display_name in concrete_imports:
                dbg_val = get_mem(a)
                name = proj._sim_procedures[state_val].display_name

                if dbg_val >= plt_end or dbg_val < plt_start:  # already resolved by the loader in the dbg
                    setattr(state.mem[a], "uint%d_t" % proj.arch.bits, dbg_val)
                else:
                    ea = debugger.resolve_name(name)
                    if ea is not None:
                        setattr(state.mem[a], "uint%d_t" % proj.arch.bits, ea)
            else:
                setattr(state.mem[a], "uint%d_t" % proj.arch.bits, state_val)

    return state


def build_bind_now_got(proj, state):
    debugger = get_debugger()

    try:
        got_start, got_end = debugger.get_got()
    except BaseException:
        l.warning("cannot find .got.plt section, build_bind_now_got failed")
        return state

    try:
        plt_start, plt_end = debugger.get_plt()
    except BaseException:
        l.warning("cannot find .plt section, build_bind_now_got failed")
        return state

    entry_len = proj.arch.bits // 8
    get_mem = debugger.get_dword if entry_len == 4 else debugger.get_qword

    got_start += 3 * entry_len  # skip first 3 entries
    
    empty_state = proj.factory.blank_state()

    for a in range(got_start, got_end, entry_len):
        state_val = empty_state.solver.eval(
            getattr(
                empty_state.mem[a],
                "uint%d_t" %
                proj.arch.bits).resolved)
        if state_val in proj._sim_procedures:
            dbg_val = get_mem(a)
            name = proj._sim_procedures[state_val].display_name

            if dbg_val >= plt_end or dbg_val < plt_start:  # already resolved by the loader in the dbg
                setattr(state.mem[a], "uint%d_t" % proj.arch.bits, dbg_val)
            else:
                ea = debugger.resolve_name(name)
                if ea is not None:
                    setattr(state.mem[a], "uint%d_t" % proj.arch.bits, ea)
    return state
