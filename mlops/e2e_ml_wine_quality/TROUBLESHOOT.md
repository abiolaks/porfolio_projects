```
remote: error: See https://gh.io/lfs for more information. remote: error: File lead_scoring_model/models/random_forest.model is 243.04 MB; this exceeds GitHub's file size limit of 100.00 MB remote: error: GH001: Large files detected. You may want to try Git Large File Storage - https://git-lfs.github.com. To https://github.com/abiolaks/porfolio_projects.git ! [remote rejected] main -> main (pre-receive hook declined) error: failed to push some refs to 'https://github.com/abiolaks/porfolio_projects.git'
```



You hit GitHub’s 100 MB hard limit because random_forest.model is ~243 MB. Fix = move large binaries to Git LFS (or keep them outside the repo) and rewrite your history so no commit contains that big file in “normal” Git.

Here’s the clean, reliable path that keeps the model in the repo via LFS:

Quick fix (use Git LFS + rewrite history)

Install and initialize LFS

git lfs install
git lfs track "*.model"
git add .gitattributes
git commit -m "Track model files via Git LFS"


Convert past commits to LFS (so no commit exceeds 100 MB)

This rewrites history to store *.model files as LFS pointers.

# Convert only your main branch history:
git lfs migrate import --include="*.model" --include-ref=refs/heads/main
# If you have other branches/tags, you can do:
# git lfs migrate import --include="*.model" --everything


Push the rewritten history

git push origin main --force


That’s it. After this, GitHub will accept the push because all .model blobs live in LFS, not regular Git.

Why this works

Problem: GitHub blocks any regular Git blob >100 MB anywhere in history.

LFS migrate: Rewrites old commits so *.model becomes lightweight pointers; the actual binary goes to LFS storage.

Force push: Required because history changed.

If you’d rather not keep the model in the repo

Remove it from Git history entirely and store it elsewhere (e.g., GitHub Releases, Azure Blob, S3):

# 1) Remove the big file from the current index
git rm --cached lead_scoring_model/models/random_forest.model
echo "lead_scoring_model/models/random_forest.model" >> .gitignore
git add .gitignore
git commit -m "Remove large model from repo; ignore going forward"

# 2) Purge it from ALL past commits (needs git-filter-repo installed)
git filter-repo --path lead_scoring_model/models/random_forest.model --invert-paths

# 3) Push rewritten history
git push origin main --force


Then host the model somewhere (e.g., Azure Blob) and add a small download script or link.

Common gotchas

If teammates have already pulled, they must re-clone or run git fetch --all --prune + reset to avoid history conflicts.

Ensure .gitattributes (with *.model filter=lfs diff=lfs merge=lfs -text) is committed before future large files are added.

For other heavy artifacts (checkpoints, parquet dumps, etc.), add patterns to LFS early: git lfs track "*.ckpt" "*.pt" "*.pkl" "*.parquet".