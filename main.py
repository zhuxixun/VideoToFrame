import cv2


def split_frames(file_path, save_path, interval_time):
    cap = cv2.VideoCapture(file_path)  # 打开视频文件
    num = 1
    seq = 1
    while True:
        success, img = cap.read()
        if not success:
            break
        if num % interval_time == 0:
            save_name = str(seq)
            cv2.imwrite(save_path + save_name + ".jpg", img)
            print(num)
        num += 1
        seq += 1
    cap.release()


if __name__ == '__main__':
    video_path = r'D:\CaptureVideo\LOL.mp4'
    save_file_path = r'D:/CaptureVideo/frames/'
    interval_time = 1
    split_frames(video_path, save_file_path, interval_time)
