# ci-info

A Python implementation of [watson/ci-info](https://github.com/watson/ci-info).
Get details about the current Continuous Integration environment.

Please [open an issue](https://github.com/mgxd/ci-info/issues/new)
if your CI server isn't properly detected :)


## Supported CI tools

Officially supported CI servers:

| Name | Constant | isPR |
|------|----------|------|
| [AWS CodeBuild](https://aws.amazon.com/codebuild/) | `ci.CODEBUILD` | 🚫 |
| [AppVeyor](http://www.appveyor.com) | `ci.APPVEYOR` | ✅ |
| [Azure Pipelines](https://azure.microsoft.com/en-us/services/devops/pipelines/) | `ci.AZURE_PIPELINES` | ✅ |
| [Bamboo](https://www.atlassian.com/software/bamboo) by Atlassian | `ci.BAMBOO` | 🚫 |
| [Bitbucket Pipelines](https://bitbucket.org/product/features/pipelines) | `ci.BITBUCKET` | ✅ |
| [Bitrise](https://www.bitrise.io/) | `ci.BITRISE` | ✅ |
| [Buddy](https://buddy.works/) | `ci.BUDDY` | ✅ |
| [Buildkite](https://buildkite.com) | `ci.BUILDKITE` | ✅ |
| [CircleCI](http://circleci.com) | `ci.CIRCLE` | ✅ |
| [Cirrus CI](https://cirrus-ci.org) | `ci.CIRRUS` | ✅ |
| [Codeship](https://codeship.com) | `ci.CODESHIP` | 🚫 |
| [Drone](https://drone.io) | `ci.DRONE` | ✅ |
| [dsari](https://github.com/rfinnie/dsari) | `ci.DSARI` | 🚫 |
| [GitLab CI](https://about.gitlab.com/gitlab-ci/) | `ci.GITLAB` | 🚫 |
| [GoCD](https://www.go.cd/) | `ci.GOCD` | 🚫 |
| [Hudson](http://hudson-ci.org) | `ci.HUDSON` | 🚫 |
| [Jenkins CI](https://jenkins-ci.org) | `ci.JENKINS` | ✅ |
| [Magnum CI](https://magnum-ci.com) | `ci.MAGNUM` | 🚫 |
| [Netlify CI](https://www.netlify.com/) | `ci.NETLIFY` | ✅ |
| [Nevercode](http://nevercode.io/) | `ci.NEVERCODE` | ✅ |
| [Sail CI](https://sail.ci/) | `ci.SAIL` | ✅ |
| [Semaphore](https://semaphoreci.com) | `ci.SEMAPHORE` | ✅ |
| [Shippable](https://www.shippable.com/) | `ci.SHIPPABLE` | ✅ |
| [Solano CI](https://www.solanolabs.com/) | `ci.SOLANO` | ✅ |
| [Strider CD](https://strider-cd.github.io/) | `ci.STRIDER` | 🚫 |
| [TaskCluster](http://docs.taskcluster.net) | `ci.TASKCLUSTER` | 🚫 |
| [TeamCity](https://www.jetbrains.com/teamcity/) by JetBrains | `ci.TEAMCITY` | 🚫 |
| [Travis CI](http://travis-ci.org) | `ci.TRAVIS` | ✅ |



## Usage

```python
import ci
if ci.is_ci():
    print(ci.name())

"My CI Name"
```


## API

### `ci.name()`

Returns a string containing name of the CI server the code is running on.
If CI server is not detected, it returns `None`.

Don't depend on the value of this string not to change for a specific
vendor.

### `ci.is_ci()`

Returns a boolean. Will be `True` if the code is running on a CI server,
otherwise `False`.

Some CI servers not listed here might still trigger the `ci.is_ci()`
boolean to be set to `True` if they use certain vendor neutral
environment variables. In those cases `ci.name()` will be `None` and no
vendor specific boolean will be set to `True`.

### `ci.is_pr()`

Returns a boolean if PR detection is supported for the current CI server. Will
be `True` if a PR is being tested, otherwise `False`. If PR detection is
not supported for the current CI server, the value will be `None`.

### `ci.info()`

Returns a dictionary of all above values in key/value pairs.

## License

[MIT](LICENSE)
