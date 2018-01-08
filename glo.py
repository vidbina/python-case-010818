from a import wave

def main(conf):
    print("in main, conf.a = %s" % conf['a'])
    wave(conf)

conf = { 'a': 12 }

main(conf)
