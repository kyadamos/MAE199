from sim_envs.GymGlucose import T1DSimEnv
from gym.envs.registration import register

'''
age_group = ['child', 'adolescent', 'adult']

for a in age_group:
    for i in range(1,11):
        print("register(")
        print("    id='simglucose-"f"{a}{i}-v0',")
        print("    entry_point='sim_envs:T1DSimEnv',")
        print("    kwargs={'patient_name':"f"'{a}#{i:03}'""}")
        print(")")
        print("\n")
'''
register(
    id='simglucose-child1-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#001'}
)


register(
    id='simglucose-child2-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#002'}
)


register(
    id='simglucose-child3-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#003'}
)


register(
    id='simglucose-child4-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#004'}
)


register(
    id='simglucose-child5-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#005'}
)


register(
    id='simglucose-child6-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#006'}
)


register(
    id='simglucose-child7-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#007'}
)


register(
    id='simglucose-child8-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#008'}
)


register(
    id='simglucose-child9-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#009'}
)


register(
    id='simglucose-child10-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'child#010'}
)


register(
    id='simglucose-adolescent1-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#001'}
)


register(
    id='simglucose-adolescent2-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#002'}
)


register(
    id='simglucose-adolescent3-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#003'}
)


register(
    id='simglucose-adolescent4-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#004'}
)


register(
    id='simglucose-adolescent5-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#005'}
)


register(
    id='simglucose-adolescent6-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#006'}
)


register(
    id='simglucose-adolescent7-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#007'}
)


register(
    id='simglucose-adolescent8-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#008'}
)


register(
    id='simglucose-adolescent9-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#009'}
)


register(
    id='simglucose-adolescent10-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adolescent#010'}
)


register(
    id='simglucose-adult1-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#001'}
)


register(
    id='simglucose-adult2-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#002'}
)


register(
    id='simglucose-adult3-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#003'}
)


register(
    id='simglucose-adult4-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#004'}
)


register(
    id='simglucose-adult5-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#005'}
)


register(
    id='simglucose-adult6-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#006'}
)


register(
    id='simglucose-adult7-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#007'}
)


register(
    id='simglucose-adult8-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#008'}
)


register(
    id='simglucose-adult9-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#009'}
)


register(
    id='simglucose-adult10-v0',
    entry_point='sim_envs:T1DSimEnv',
    kwargs={'patient_name':'adult#010'}
)