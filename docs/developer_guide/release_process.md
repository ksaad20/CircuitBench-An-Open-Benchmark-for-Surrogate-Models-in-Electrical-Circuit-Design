# Release Process

## Overview

This document describes the release workflow for Circuit-Bench. The objective is to ensure every release is reproducible, well documented, and scientifically reliable.

---

# Release Philosophy

Each release should:

* Be reproducible
* Pass all automated tests
* Include complete documentation
* Preserve backward compatibility where practical
* Provide clear release notes
* Be permanently identifiable through version tags

---

# Versioning

Circuit-Bench follows Semantic Versioning.

Format:

```
MAJOR.MINOR.PATCH
```

Examples:

* 1.0.0
* 1.1.0
* 1.1.1

Guidelines:

* **MAJOR** – incompatible API or benchmark changes
* **MINOR** – new features, datasets, or benchmark tasks
* **PATCH** – bug fixes, documentation updates, and minor improvements

---

# Release Checklist

Before creating a release:

* All tests pass
* CI succeeds
* Documentation is up to date
* Dataset metadata validated
* Licenses reviewed
* Benchmark metrics verified
* Version number updated
* Changelog completed

---

# Pre-release Validation

Verify:

* Dataset integrity
* Schema validation
* Benchmark reproducibility
* Example commands
* CLI functionality
* Installation instructions
* Download links

---

# Creating a Release

Typical workflow:

1. Merge approved changes into the main branch.
2. Update version information.
3. Update the changelog.
4. Create a Git tag.
5. Publish the GitHub release.
6. Archive release artifacts when applicable.

---

# Release Notes

Release notes should include:

* New features
* New datasets
* Benchmark improvements
* Bug fixes
* Breaking changes
* Documentation updates
* Known limitations

---

# Dataset Releases

For dataset updates:

* Validate metadata
* Verify checksums
* Confirm licensing
* Record provenance
* Update dataset documentation

---

# Benchmark Releases

Benchmark releases should document:

* Supported tasks
* Evaluation protocols
* Baseline methods
* Metrics
* Dataset versions
* Compatibility information

---

# Quality Assurance

Before publication:

* Run the complete test suite.
* Review benchmark outputs.
* Verify documentation links.
* Confirm reproducibility.
* Validate release artifacts.

---

# Archiving

Each release should be archived with:

* Version identifier
* Release notes
* Dataset metadata
* Citation information
* License information

Persistent archival services (for example, Zenodo) are recommended for citable releases.

---

# Rollback

If a critical issue is discovered:

* Identify the affected release.
* Document the issue.
* Publish a corrective release.
* Notify users through the release notes.

Avoid modifying published release artifacts whenever possible.

---

# Responsibilities

Maintainers are responsible for:

* Reviewing release readiness
* Approving changes
* Publishing releases
* Maintaining documentation
* Ensuring reproducibility

Contributors should ensure that submitted changes include appropriate tests and documentation.

---

# Continuous Improvement

The release process should be reviewed periodically and updated as Circuit-Bench evolves, incorporating community feedback and improvements to reproducibility, documentation, and benchmarking practices.

