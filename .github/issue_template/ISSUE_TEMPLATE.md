---
name: Someone just pushed
labels: ''
assignees: YaSwe
---

**Issue Description:**

Someone just pushed, oh no! Here's who did it: `{{ payload.sender.login }}`.

**Context:**

- [Failed Run](https://github.com/${{ github.repository }}/actions/runs/${{ github.run_id }})
- [Codebase](https://github.com/${{ github.repository }}/tree/${{ github.sha }}})
- Workflow name: `${{ github.workflow }}`
- Job: `${{ github.job }}`
- Status: `${{ job.status }}`
