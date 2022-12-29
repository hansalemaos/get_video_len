import cv2


def get_video_len_and_frames(videofile):
    try:
        video = cv2.VideoCapture(videofile)
        frame_rate = video.get(cv2.CAP_PROP_FPS)
        total_num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = total_num_frames / frame_rate
        return {
            "file_path": videofile,
            "duration": duration,
            "total_frames": total_num_frames,
            "frame_rate": frame_rate,
        }
    except Exception:
        return {
            "file_path": videofile,
            "duration": None,
            "total_frames": None,
            "frame_rate": None,
        }

