# Gets the duration, frame rate and total frames from a video file 

```python
$pip install get-video-len

from pprint import pprint
from get_video_len import get_video_len_and_frames
videoinfos = get_video_len_and_frames(videofile=r"F:\convertedvideossocialnet\newvidxx2.mp4")
pprint(videoinfos)
 {'duration': 139.83983983983984,
  'file_path': 'F:\\convertedvideossocialnet\\newvidxx2.mp4',
  'frame_rate': 29.97,
  'total_frames': 4191.0}

```




