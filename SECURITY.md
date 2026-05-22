# Security Policy

## Overview

This document outlines the security policy for the **Student Management System** project,
covering both the **Python** and **Java** implementations. It defines which runtime
versions are actively supported and which are considered end-of-life (EOL), and provides
guidance on reporting vulnerabilities.

---

## Supported Versions

The table below lists which versions of Python and Java are known to **work** with this
project, and whether they receive security support.

### Python Version

| Python Version | Status                  | Notes                                                      |
|----------------|-------------------------|------------------------------------------------------------|
| 3.13.x         | ✅ Fully Supported       | Recommended. Actively maintained by the Python core team.  |
| 3.12.x         | ✅ Fully Supported       | Actively maintained.                                       |
| 3.11.x         | ✅ Fully Supported       | Security fixes only from the Python core team.             |
| 3.10.x         | ✅ Fully Supported       | Security fixes only from the Python core team.             |
| 3.9.x          | ⚠️ Works / Out of Support | Functional with this project. **EOL: October 2025.** No upstream security patches. |
| 3.8.x          | ⚠️ Works / Out of Support | Functional with this project. **EOL: October 2024.** No upstream security patches. |
| < 3.8          | ❌ Not Supported          | Not tested. Not compatible. Do not use.                    |

> **Minimum recommended version**: Python **3.10** or higher.

---

### Java Version

| JDK Version    | Status                  | Notes                                                              |
|----------------|-------------------------|--------------------------------------------------------------------|
| JDK 24         | ✅ Fully Supported       | Current release. Recommended for development.                      |
| JDK 21 (LTS)   | ✅ Fully Supported       | Long-Term Support. Recommended for production.                     |
| JDK 17 (LTS)   | ✅ Fully Supported       | Long-Term Support. Widely used, security patches available.        |
| JDK 11 (LTS)   | ⚠️ Works / Out of Support | Functional with this project. **Oracle EOL: September 2023 (free).** Community builds (e.g., Adoptium) may still receive patches — verify your vendor. |
| JDK 8 (LTS)    | ⚠️ Works / Out of Support | Functional with this project. **Oracle EOL: March 2022 (free).** Widely deployed legacy version. Community/vendor patches vary significantly. |
| JDK < 8        | ❌ Not Supported          | Not tested. Not compatible. Do not use.                            |

> **Minimum recommended version**: JDK **17 (LTS)** or higher for new deployments.

---

## ⚠️ Notice on Out-of-Support Versions

Versions marked **"Works / Out of Support"** (Python 3.8, 3.9 and JDK 8, 11) have the
following important caveats:

- They **function correctly** with this project at the time of testing.
- They **no longer receive security patches** from their upstream maintainers.
- Any newly discovered CVEs in those runtimes **will not be patched** by Python core or
  Oracle/OpenJDK upstream.
- Dependencies (e.g., `mysql-connector-python`, `matplotlib`, Maven packages) may also
  drop support for older runtimes over time, creating additional attack surface.
- **Use of these versions in production environments is strongly discouraged.**

If you are constrained to running an out-of-support runtime, consider:
1. Isolating the application in a network-restricted environment.
2. Applying OS-level firewall rules to limit database exposure.
3. Keeping all third-party libraries updated within compatible ranges.
4. Planning a migration to a supported runtime version as soon as feasible.

---

## Reporting a Vulnerability

If you discover a security vulnerability in **this project's own code** (not in the
underlying Python/Java runtimes), please follow the responsible disclosure process below.

### How to Report

1. **Do NOT open a public GitHub Issue** for security vulnerabilities.
2. Use **GitHub's private vulnerability reporting** feature:
   - Navigate to the **Security** tab of this repository.
   - Click **"Report a vulnerability"**.
   - Fill in the details and submit.
3. Alternatively, contact the maintainer directly via the email listed in the repository
   profile.

### What to Include

Please provide as much of the following information as possible to help us triage and
resolve the issue quickly:

- **Description** of the vulnerability and its potential impact.
- **Steps to reproduce** (proof-of-concept code or commands if applicable).
- **Affected versions** (Python or Java edition, runtime version).
- **Suggested fix** (optional but appreciated).

### Response Timeline

| Step                         | Target Timeframe      |
|------------------------------|-----------------------|
| Initial acknowledgement      | Within **72 hours**   |
| Severity assessment          | Within **7 days**     |
| Fix or mitigation released   | Within **30 days**    |
| Public disclosure            | After fix is released |

---

## Dependency Security

This project uses the following key dependencies that should be kept up to date:

### Python Dependencies

| Package                  | Purpose                  | Update Channel   |
|--------------------------|--------------------------|------------------|
| `mysql-connector-python` | MySQL database driver    | PyPI / Dependabot |
| `matplotlib`             | Data visualization       | PyPI / Dependabot |
| `python-dotenv`          | Environment variable loading | PyPI / Dependabot |

### Java / Maven Dependencies

| Artifact                   | Purpose                  | Update Channel   |
|----------------------------|--------------------------|------------------|
| `mysql-connector-java`     | MySQL database driver    | Maven Central    |
| `flatlaf`                  | Modern Swing look & feel | Maven Central    |
| `jfreechart`               | Chart rendering          | Maven Central    |

Dependabot is configured to automatically open pull requests for outdated Python (`pip`)
dependencies. For Java/Maven, manually review `pom.xml` periodically or enable Maven
ecosystem updates in `.github/dependabot.yml`.

---

## Additional Security Recommendations

- **Never commit credentials**: Use `.env` files (already in `.gitignore`) and never
  hardcode database passwords in source code.
- **Use least-privilege database accounts**: Grant only `SELECT`, `INSERT`, `UPDATE`,
  `DELETE` on `school_db` — not `GRANT`, `DROP`, or `CREATE`.
- **Restrict database network access**: Bind MySQL to `127.0.0.1` (localhost) unless a
  remote connection is explicitly required.
- **Keep your OS and runtime patched**: Regardless of the application's version support,
  always apply OS-level and JVM/Python runtime security patches.

---

*Last updated: May 2026*
