import sys
import logging
from collections import defaultdict
from bw import BWReader
import thinkgear
from datetime import datetime

logging.basicConfig(stream=sys.stdout,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# setting thinkgear logger level to INFO
_log = logging.getLogger(__name__)
logging.getLogger('thinkgear').setLevel(logging.INFO)

metrics_to_show = (
    thinkgear.ThinkGearMeditationData,
    thinkgear.ThinkGearAttentionData,
    thinkgear.ThinkGearPoorSignalData
)

code_to_title = {
    thinkgear.ThinkGearMeditationData.code: 'Meditation',
    thinkgear.ThinkGearAttentionData.code: 'Attention',
    thinkgear.ThinkGearPoorSignalData.code: 'Poor Signal'
}


def output_data(data):
    print '[{:%H:%M:%S}]>'.format( datetime.now())
    for m in metrics_to_show:
        print '{}\t:{}'.format(code_to_title[m.code], data[m.code])



def main():
    # instructions are: connect device using UI, then execute:
    # make sure using your device address and port
    reader = BWReader('00:13:EF:00:4F:F2', 3)
    data = defaultdict(int)
    for packet in reader.get_packets():
        if isinstance(packet, thinkgear.ThinkGearRawWaveData):
            continue
        elif isinstance(packet, metrics_to_show):
            _log.debug('got data %s', packet)

            if data[packet.code] != packet.value:
                data[packet.code] = packet.value
                output_data(data)


if __name__ == '__main__':
    main()