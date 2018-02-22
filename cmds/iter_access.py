import os
import pathlib
import time

# TODO: change part that saves fastq files to the top-level dir of LU-microbiome.
# A script for automating the download of SRA files using Accession #s.

# TODO: Add option to have files delete themselves after finishing.

def sra_to_fastq(toolpath, outdir, compress=False):
    print('CONVERTING SRA TO FASTQ...')
    fastq_dirpath = os.path.join(toolpath, outdir)
    pathlib.Path(fastq_dirpath).mkdir(parents=True, exist_ok=True)
    # TODO: decide if you want to keep ^this^ path creation command as
    #  it currently is. Might be safer to change args to "false",
    # but in that case, you should make a funciton the user can use
    #  to clear the data from the fastq data folder, otherwise
    # they're going to get errors if the function tries to make a
    # folder with the same name as an existing one. Alternatively,
    # just have documentation that tells users to go into file
    # directory and delete fastq data by hand.

    # TODO: find way to not have the sra directory hard-coded.
    sra_dir_path = '/Volumes/Gniot_Backup_Drive/repos/LU-microbiome/sequencedata/sratool_workspace/sra'
    for base, dirs, files in os.walk(sra_dir_path):
        for fname in files:
            if fname.split('.')[-1] == 'sra':
                t0 = time.time()
                if compress:
                    os.system(
                        "fastq-dump --gzip --outdir " + fastq_dirpath + " " + os.path.join(base, fname))
                else:
                    os.system(
                        "fastq-dump --outdir " + fastq_dirpath + " " + os.path.join(
                            base, fname))
                t1 = time.time()
                print('SRA CONVERTED TO FASTQ IN ' + str(t1 - t0))
                os.remove(os.path.join(base, fname))

def get_sra(toolpath, acc_dir, compress=False):
    t0 = time.time()
    comp = compress
    accession_dir = os.path.join(toolpath, acc_dir)
    for base_dirpath, dirnames, filenames in os.walk(accession_dir):
        for fname in filenames:
            if fname == '.DS_Store':
                continue
            if 'SRR_Acc' in fname:
                print('Opening file: ' + fname)
                # Open accession number file.
                with open(os.path.join(base_dirpath, fname), 'r') as f:
                    print('\tStarting .sra download...')
                    for sra in f.readlines():
                        os.system('prefetch ' + sra)
                t1 = time.time()
                print('\tSRA DOWNLOAD COMPLETED IN ' + str(t1 - t0))

                fastq_dir = 'sequencedata/fastq/' + fname.split('_')[-1].split('.')[0]
                sra_to_fastq(toolpath, fastq_dir, compress=comp)


# get_sra('predata')