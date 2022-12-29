import cv2


def get_video_len_and_frames(videofile):
    try:
        video = cv2.VideoCapture(videofile)
        frame_rate = video.get(cv2.CAP_PROP_FPS)
        total_num_frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
        duration = total_num_frames / frame_rate
        IMG_H = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        IMG_W = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        return {
            "file_path": videofile,
            "duration": duration,
            "total_frames": total_num_frames,
            "frame_rate": frame_rate,
            "width": IMG_W,
            "height": IMG_H,
        }
    except Exception:
        return {
            "file_path": videofile,
            "duration": None,
            "total_frames": None,
            "frame_rate": None,
            "width": None,
            "height": None,
        }
