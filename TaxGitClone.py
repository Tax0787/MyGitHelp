o=open
with o('temp.sh','w')as f:
    you=input("You'r Github NickName : ")
    repo=input("You'r repo name : ")
    source=f"gi
    
    qt clone https://github.com/{you}/{repo}.git"
    input(f'sourse is : "{source}" > ')
    f.write(source)
