experiments_repo = Artifact.registerArtifact(
    command = '''
        git clone https://gem5.googlesource.com/public/gem5-resources
        cd gem5-resources
        git checkout 1fe56ffc94005b7fa0ae5634c6edc5e2cb0b7357
        cd src/spec-2017
        git init
        git remote add origin https://remote-address/spec-experiment.git
    ''',
    typ = 'git repo',
    name = 'spec2017 Experiment',
    path =  './',
    cwd = './',
    documentation = '''
        local repo to run spec 2017 experiments with gem5 full system mode;
        resources cloned from https://gem5.googlesource.com/public/gem5-resources upto commit 1fe56ffc94005b7fa0ae5634c6edc5e2cb0b7357 of stable branch
    '''
)

