import os
# import con
home = "/Volumes/Gniot_Backup_Drive/repos/LU-microbiome/sequencedata/fastq"
for root, dirs, files in os.walk(home):
    for dir in dirs:
        print(dir)
        for root2, dirs2, files2 in os.walk(os.path.join(home, dir)):
            for fname in files2:
                out_folder = root2.split("/")[-1]
                out_folder_home = "/Volumes/Gniot_Backup_Drive/repos/LU-microbiome/sequencedata/fastqc_filtrim"
                out_dir = os.path.join(out_folder_home, out_folder)
                os.system((trim_galore --quality 20 --fastqc --nextera --stringency 3 --length 20 --clip_R1 5 --output_dir out_dir os.path.join(root2, fname)))
                break