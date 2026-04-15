Reproduced on Visual Studio Professional 18.4.1 (March 2026 Feature Update).

## Enable diagnostic logging

In Visual Studio, open TOOLS -> "Options...", and set the logging level for tests to "Diagnostic", as shown in the screenshot:

<img width="1033" height="752" alt="image" src="https://github.com/user-attachments/assets/0f0b6e67-adb4-4081-8ad6-ad040cb275de" />

## Reproduce issue

Every time a test is run from the Test Explorer, the Tests output contains log lines similar to these:

```
[15.04.2026 1:17:43.005 p.m.]  Test run progress has started.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.TestPlatform.TestHost' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'NUnit' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.Testing.Extensions.VSTestBridge' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.Testing.Platform' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.TestPlatform.ObjectModel' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.Testing.Extensions.Telemetry' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.CodeCoverage' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.NET.Test.Sdk' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'NUnit3TestAdapter' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'altcover' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.Testing.Platform.MSBuild' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.Testing.Extensions.TrxReport.Abstractions' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'coverlet.collector' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.080 p.m.]  Failed to determine installation location for NuGet package 'Microsoft.ApplicationInsights' referenced in project 'VSTestIssueReproTests'. Check to make sure that a NuGet restore operation has been performed for this project and that no errors were reported during this operation.
[15.04.2026 1:17:43.480 p.m.]  ========== Starting test run ==========
```

If the solution contains multiple projects, the delay caused by the "Failed to determine installation location for NuGet package" log lines may be **many seconds** long.
