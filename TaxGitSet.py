a=lambda x:f'git config --global user.{x}'
bN=lambda x:a(f'name "{x}"')
bE=lambda x:a(f'email "{x}"')
SI=lambda x:str(input(x))
o=open
with o('TaxGitSet.sh','w')as f:
    source=bN(SI('name : '))+'\n'+bE(SI('e-mail : '))
    input(f'sourse is : "{source}" > ')
    f.write(source)