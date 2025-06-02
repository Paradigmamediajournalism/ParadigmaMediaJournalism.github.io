from moviepy.editor import VideoFileClip, clips_array

# Muat dan resize semua video
clip1 = VideoFileClip("WE.mp4").resize(width=720)
clip2 = VideoFileClip("New.mp4").resize(width=720)
clip3 = VideoFileClip("WES.mp4").resize(width=720)
clip4 = VideoFileClip("TEWAS.mp4").resize(width=720)

# Samakan durasi agar sinkron
min_duration = min(clip1.duration, clip2.duration, clip3.duration, clip4.duration)
clip1 = clip1.subclip(0, min_duration)
clip2 = clip2.subclip(0, min_duration)
clip3 = clip3.subclip(0, min_duration)
clip4 = clip4.subclip(0, min_duration)

# Gabungkan dalam satu layar vertikal (dari atas ke bawah)
final = clips_array([[clip1], [clip2], [clip3], [clip4]])

# Simpan hasilnya
final.write_videofile("video_vertikal.mp4")
