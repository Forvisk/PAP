

int main(){
env = Environment()
    conf = Configure(env)
    if not conf.CheckCXXHeader('vector.h'):
        print 'vector.h must be installed!'
        Exit(1)
    env = conf.Finish()}