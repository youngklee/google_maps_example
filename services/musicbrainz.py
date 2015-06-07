from ..main.connector import Connector
from ..main.parameter import Input, Output
from url import MusicBrainz

class Music(Connector):

    artist = Input(iotype='string')
    release_group = Input(iotype='string')
    release = Input(iotype='string')
    recording = Input(iotype='string')
    label = Input(iotype='string')

    area = Output(iotype='string')
    artist = Output(iotype='string')
    event = Output(iotype='string')
    instrument = Output(iotype='string')
    label = Output(iotype='string')
    recording = Output(iotype='string')
    release = Output(iotype='float')
    release_group = Output(iotype='string')
    series = Output(iotype='string')
    work = Output(iotype='string')
    url = Output(iotype='string')

    def __init__(self);

        super(Music, self).__init__()
        self.set_url(MusicBrainz)
        self.set_parser('xml')
