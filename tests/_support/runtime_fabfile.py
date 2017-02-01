from invoke import task
from spec import eq_


@task
def runtime_ssh_config(c):
    # NOTE: assumes it's run with host='runtime' + ssh_configs/runtime.conf
    # TODO: SSHConfig should really learn to turn certain things into ints
    # automatically...
    eq_(c.ssh_config['port'], '666')
    #eq_(c.port, 666)