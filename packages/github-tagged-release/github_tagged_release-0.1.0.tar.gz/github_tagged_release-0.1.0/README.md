## GitHub tagged release
GitHub changelogs using tags for your CircleCI workflow.

### Usage
```bash
pip install github_tagged_release
github_tagged_release
```

#### In python
```python
from github_release import GitHubRelease
gr = GitHubRelease()
gr.create_release_from_tag()
```

Example CircleCI workflow:
```yaml
version: 2
jobs:
  build:
    docker:
      - image: circleci/node:8
    steps:
      - checkout
      - npm install
      - npm test

   deploy_prod:
    docker:
      - image: circleci/node:8
    steps:
      - run:
          name: Verify tag on master branch
          command: |
            git branch --contains | grep -q '^[ |*] master$'
      - run:
          name: Deploy
          command: npm run deploy
      - run:
          name: Create GitHub release
          command: |
            pip install --user github-tagged-release
            python ~/.local/bin/github_tagged_release
workflows:
  version: 2
  build_test_hold_deploy:
    jobs:
      - build:
          filters:
            tags:
              only: /.*/
      - deploy_prod:
          requires:
            - build
          filters:
            tags:
              only: /^v[0-9]+(\.[0-9]+)*$/
            branches:
              ignore: /.*/
```