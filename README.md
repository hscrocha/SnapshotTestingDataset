# SnapshotTestingDataset

This is a dataset of GitHub repositories that were tagged with Jest, for JS or TS languages, that used Snapshot Testing. Information on all repositories is available in the file "0_Snapshot Testing Dataset.xlsx" (named to be the very first file on Zenodo, here it is located on the root folder). 

In the folder 'repos_targz', you will find all compact targz files representing repository as "<github_username>_<repository_name>.tar.gz". We split large repositories (>50MB) using the "split" command on Unix-type shell (use cat to rejoin them). 

In total there are 686 repositories. We collected only public repositories that were tagged with the Jest keyword, for JavaScript or Typescript, had at least 1 star, and at least 1 snapshot file. The spreadsheet data was collected on July 13, 2022.

In the folder 'gathering_scripts', we have all scripts used to gather this data. There the subfolder "python" has all python scripts to find repositories based on queries and save their attributes, and "node_and_shell" contain the node and shell scripts to download a tarball of the repository. Therefore you should first use the python scripts to collect repositories & their attribute, and later use the node & shell to download a copy of the repositories. Moreover, inside each script folder there is a Readme file with instructions and examples.

This GitHub repository is an exact copy of a persistent archieved version on Zenodo (https://zenodo.org/record/7724641). But it is much better organizef into folders here on GitHub, additionally, the README files display better here.
