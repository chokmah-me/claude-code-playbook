# Migration Plan: claude-code-playbook → chokmah-me

## Overview
Migrate `dyb5784/claude-code-playbook` to `chokmah-me/claude-code-playbook` preserving full history, all 8 tags (v3.0.0–v4.1.3), branches, GitHub Actions, issue templates, and repository metadata.

## Prerequisites ✓ (Verified)
- ✓ GitHub CLI authenticated: chokmah-me (active), dyb5784, indranet-admin (all in keyring)
- ✓ Scopes verified: admin:org, repo on both accounts
- ✓ No namespace conflict: `claude-code-playbook` available in chokmah-me
- ✓ Source repo healthy: 170KB, MIT licensed, v4.1.3 current

## Recommended Approach: GitHub Native Transfer

**Why `gh repo transfer` (not mirror clone):**
- Preserves ALL metadata: releases, workflow logs, issue templates, settings
- Single atomic operation (minimal downtime)
- Automatic redirect from old URL for 400+ days
- GitHub handles branch protection rules, webhooks, collaborators
- Reversible via backup mirror

## Execution Plan

### Phase 1: Pre-Migration Backup (Safety Net)

```bash
# Create complete backup mirror
git clone --mirror https://github.com/dyb5784/claude-code-playbook.git backup-mirror.git

# Verify all refs captured
cd backup-mirror.git
git show-ref | wc -l  # Should show all 8 tags + branches
cd ..
```

### Phase 2: Execute Transfer

```bash
# Ensure authenticated as account with admin on source repo
gh auth switch --user dyb5784

# Execute transfer (irreversible, requires confirmation)
gh repo transfer dyb5784/claude-code-playbook chokmah-me --yes

# Verify transfer completed
gh repo view chokmah-me/claude-code-playbook --json name,owner,pushedAt
```

**Expected outcome:**
- Repository immediately available at `https://github.com/chokmah-me/claude-code-playbook`
- Old URL redirects automatically
- All releases, tags, branches, actions preserved

### Phase 3: Verify Transfer Integrity

```bash
# Switch to chokmah-me account
gh auth switch --user chokmah-me

# Verify all 8 tags present
gh release list --repo chokmah-me/claude-code-playbook | wc -l

# Verify branches
gh api repos/chokmah-me/claude-code-playbook/branches --jq '.[].name'

# Check GitHub Actions workflows
gh api repos/chokmah-me/claude-code-playbook/actions/workflows --jq '.workflows[].name'

# Test clone
git clone https://github.com/chokmah-me/claude-code-playbook.git test-clone
cd test-clone
git tag -l | wc -l  # Should show 8
git log --oneline | head -5
cd ..
```

### Phase 4: Update Documentation References

**Critical files requiring updates:**

#### 1. README.md (4 references)
```
Find: https://github.com/dyb5784/claude-code-playbook
Replace: https://github.com/chokmah-me/claude-code-playbook

Locations:
- Clone command: git clone https://github.com/dyb5784/...
- Repository link in introduction
- Issues link: .../dyb5784/.../issues
- Discussions link: .../dyb5784/.../discussions
```

#### 2. CONTRIBUTING.md (2 references)
```
Find: https://github.com/dyb5784/claude-code-playbook
Replace: https://github.com/chokmah-me/claude-code-playbook

Plus: Update maintainer @dyb5784 → @chokmah-me (if ownership transfer)
```

#### 3. GITHUB_SETUP.md (4 references + DOI removal)
```
Find & Replace:
- Username: dyb5784 → chokmah-me
- HTTPS: https://github.com/dyb5784/claude-code-playbook.git → chokmah-me
- SSH: git@github.com:dyb5784/claude-code-playbook.git → chokmah-me

Remove:
- Zenodo DOI reference: https://doi.org/10.5281/zenodo.17744054
  (User migrated to OSF)
```

#### 4. Search for Additional References
```bash
# Comprehensive search for any remaining dyb5784 references
cd test-clone
grep -r "dyb5784" . --include="*.md" --include="*.yml" --include="*.yaml" --include="*.json"

# Check GitHub Actions for hardcoded org references
grep -r "dyb5784" .github/workflows/
```

### Phase 5: Apply Documentation Updates

```bash
cd test-clone
git checkout -b chore/migrate-org-references

# Edit files (use Claude Code Edit tool or manual editor)
# - README.md
# - CONTRIBUTING.md
# - GITHUB_SETUP.md
# - Any files found in grep search

# Verify changes
git diff --color-words

# Commit
git add README.md CONTRIBUTING.md GITHUB_SETUP.md
git commit -m "chore: update repository URLs for chokmah-me organization

- Updated clone URLs in README.md
- Updated fork workflow in CONTRIBUTING.md
- Updated setup guide in GITHUB_SETUP.md
- Removed Zenodo DOI (migrated to OSF)

Repository transferred from dyb5784 to chokmah-me organization."

# Push and merge
git push origin chore/migrate-org-references
gh pr create --title "Update repository URLs for org migration" \
  --body "Updates documentation to reflect transfer to chokmah-me organization"
gh pr merge --squash --delete-branch
```

### Phase 6: Configure Repository Metadata

```bash
# Apply repository topics (7 total from source)
gh repo edit chokmah-me/claude-code-playbook \
  --add-topic claude-ai \
  --add-topic ai-development \
  --add-topic refactoring \
  --add-topic typescript \
  --add-topic developer-tools \
  --add-topic workflows \
  --add-topic token-optimization

# Verify description
gh repo edit chokmah-me/claude-code-playbook \
  --description "Practitioner's Playbook for Claude Code: Configuration for Token-Efficient AI Engineering"
```

### Phase 7: Handle Source Repository

**Recommended: Archive dyb5784/claude-code-playbook**

```bash
# Switch to dyb5784 account
gh auth switch --user dyb5784

# Archive (makes read-only, preserves redirect)
gh repo archive dyb5784/claude-code-playbook --yes
```

**Why archive (not delete):**
- Preserves historical reference
- GitHub redirect continues working
- Prevents accidental pushes to old location
- Clear deprecation signal
- No infrastructure cost

**Alternative: Add deprecation notice to old repo README**
```bash
# If old repo still accessible, prepend notice
# (Only if transfer failed or you kept separate copy)
echo "# ⚠️ ARCHIVED - Repository Moved
This repository has migrated to [chokmah-me/claude-code-playbook](https://github.com/chokmah-me/claude-code-playbook).

Please update your bookmarks and local clones." > DEPRECATION_NOTICE.md
```

### Phase 8: Post-Migration Verification

```bash
# Test end-to-end workflow
git clone https://github.com/chokmah-me/claude-code-playbook.git fresh-clone
cd fresh-clone

# Verify
git tag -l  # All 8 tags present
git log --oneline | head -10  # Commit history intact
git branch -a  # All branches present

# Test GitHub Actions (if applicable)
gh workflow list --repo chokmah-me/claude-code-playbook

# Verify documentation renders
gh repo view chokmah-me/claude-code-playbook --web
```

## Critical Files Reference

### Must Update:
1. **README.md** - 4 URL references (clone, repo link, issues, discussions)
2. **CONTRIBUTING.md** - 2 references (fork workflow, maintainer)
3. **GITHUB_SETUP.md** - 4 references + Zenodo DOI removal

### GitHub Actions (Check for hardcoded refs):
- `.github/workflows/*.yml` - Search for `dyb5784` in workflow files

### No Changes Needed:
- `CLAUDE.md` - Uses relative paths only
- `templates/` - No hardcoded URLs
- `scripts/` - Local paths only
- `docs/` - Relative references
- `.cursorrules`, `.gitignore` - Universal configs

## Rollback Plan

If critical issues discovered:

1. **Restore from backup mirror:**
   ```bash
   cd backup-mirror.git
   git push --mirror https://github.com/dyb5784/claude-code-playbook.git
   ```

2. **Delete failed migration:**
   ```bash
   gh repo delete chokmah-me/claude-code-playbook --yes
   ```

3. **Re-attempt transfer** after resolving issues

## Post-Migration Checklist

- [ ] All 8 tags verified (v3.0.0 → v4.1.3)
- [ ] Main branch matches source
- [ ] GitHub Actions workflows present
- [ ] Issue templates configured
- [ ] All documentation URLs updated
- [ ] Repository topics applied
- [ ] README/docs render correctly on GitHub
- [ ] No remaining `dyb5784` references in docs
- [ ] Zenodo DOI removed from GITHUB_SETUP.md
- [ ] Source repo archived
- [ ] Old URL redirects to new location

## User Communication Template

Add to README after migration (optional):

```markdown
## 📢 Repository Migration Notice

This repository migrated from `dyb5784/claude-code-playbook` to `chokmah-me/claude-code-playbook`.

**Update your local clones:**
\`\`\`bash
git remote set-url origin https://github.com/chokmah-me/claude-code-playbook.git
git fetch origin
\`\`\`

All releases, issues, and history are preserved. The old URL redirects automatically.
```

## Estimated Execution Time

- Phase 1 (Backup): 5 minutes
- Phase 2 (Transfer): 2 minutes
- Phase 3 (Verification): 5 minutes
- Phase 4-5 (Documentation): 20 minutes
- Phase 6-7 (Metadata/Archive): 5 minutes
- Phase 8 (Final verification): 5 minutes

**Total: ~45 minutes** (conservative estimate with safety checks)
