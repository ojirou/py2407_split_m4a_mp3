import os
from pydub import AudioSegment
def split_and_convert_audio(input_file, output_folder):
    audio = AudioSegment.from_file(input_file)
    file_size_mb = os.path.getsize(input_file) / (1024 * 1024)
    size = input('分割後のmp3ファイル上限サイズを入力してください [MB] >> ')
    max_size_mb = float(size)
    segment_duration = len(audio) * (max_size_mb / file_size_mb)
    num_segments = int(file_size_mb // max_size_mb) + 1
    for i in range(num_segments):
        start_time = i * segment_duration
        end_time = start_time + segment_duration
        segment = audio[start_time:end_time]
        output_file = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_file))[0]}_{i+1}.mp3")
        segment.export(output_file, format="mp3")
def process_files_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".m4a"):
            input_file = os.path.join(folder_path, filename)
            output_folder = folder_path
            split_and_convert_audio(input_file, output_folder)
if __name__ == "__main__":
    print('ファイル分割したいm4aファイルが入ったフォルダを入力してください')
    folder_path = input('>> ')
    process_files_in_folder(folder_path)