import cmds.iter_access
import cmds.prune_sra
import time


t0 = time.time()

top = '/Volumes/Gniot_Backup_Drive/repos/LU-microbiome'
prefilt_dir = 'sequencedata/prefilter'
postfilt_dir = 'sequencedata/postfilter'

cmds.prune_sra.reduce_sra_runs(top, prefilt_dir, postfilt_dir)
cmds.iter_access.get_sra(top, postfilt_dir, compress=False)

t1 = time.time()
total = t1-t0
print(total)