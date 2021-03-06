init python:
    persistent._clear()
    config.use_cpickle = True
    renpy.music.register_channel("one", mixer="music", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    renpy.music.register_channel("two", mixer="sound", loop=None, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
    _preferences.set_volume('music', 0.5)
    _preferences.set_volume('sound', 0.2)


    def BGstr_chap():
        global location
        global chapter
        global sequence
        OutputStr = "Backgrounds/{}_{}_{}.jpg".format(location, chapter, sequence)
        if renpy.loadable(OutputStr):
            return OutputStr
        OutputStr = "Backgrounds/{}_{}.jpg".format(location, chapter)
        if renpy.loadable(OutputStr):
            return OutputStr
        OutputStr = "Backgrounds/{}.jpg".format(location)
        if renpy.loadable(OutputStr):
            return OutputStr
        return "Backgrounds/background.jpg"
