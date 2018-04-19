import os
import pandas as pd


def reduce_sra_runs(tool_path, indir, outdir):
    """
    This is a function for filtering SRA RunInfo tables and Accession Lists
    to fewer (currently: 3) runs per subject.
    This function walks through the files in the input directory, filters the
    runs, then outputs the resulting files to the output directory.
    """
    # TODO: make tool walk from top-level dir through all dirs to find indir
    # specified by user. That way, user doesn't need to specify full path for
    # indir and outdir, they can just write the name of the dir and the tool
    # will find it on its own. More user-friendly
    # ^^^Solved???^^^ (i'm not sure...)

    home = tool_path
    for root, dirnames, filenames in os.walk(os.path.join(home, indir)):
        for fname in filenames:
            if 'SraRunTable' in fname:  # For each SraRunTable file...
                # TODO: fix these two naming schemes below; won't work for
                # an automated pipeline, if I ever get that far.
                new_sratable_name = fname
                new_accession = fname.split('_')[-1]
                # Read csv file into pandas dataframe
                df = pd.read_csv(os.path.join(root, fname), delimiter='\t')

                # Get subject ids
                subject_ids = []
                for sid in df['host_subject_id']:
                    if sid not in subject_ids:
                        subject_ids.append(sid)

                # Get separate data frame for each subject
                frames = []
                for sid in subject_ids:
                    bool_index = df['host_subject_id'] == sid
                    newdf = df[bool_index]
                    frames.append(newdf)

                # Get the first 3 runs from each frame and combine them
                final = pd.concat([frame[0:3] for frame in frames])
                # Write filtered RunTable to new file
                final.to_csv(os.path.join(home, outdir, new_sratable_name),
                             sep='\t', header=True, index=False)
                # Write final accession numbers to new file
                final['Run'].to_csv(os.path.join(home, outdir, 'SRR_Acc_' + new_accession),
                                    header=False, index=False)

# prune_sra('/Volumes/Gniot_Backup_Drive/repos/LU-microbiome', 'prefilter', 'postfilter')