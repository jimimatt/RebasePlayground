# Rebase exercise repository

This repository is meant to be used as a [git](https://xkcd.com/1597/) playground to get familiar & comfy with [git rebase](https://www.youtube.com/watch?v=nHcfoHOW4uA).

**Objective**: a clean linear git history

- incorporate all feature (branches)
- reorder and/or squash commits if needed
- avoid merge commits

### Tutorials

Honourable mentions:
- atlassian [Git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/git-rebase)
- Philomatics [git rebase - Why, When & How to fix conflicts](https://www.youtube.com/watch?v=DkWDHzmMvyg)
- GitKraken [What is Git Rebase? [Intermediate Git Tutorial]](https://www.youtube.com/watch?v=_UZEXUrj-Ds)

### Best practice

Some thoughts about *commits* (discussable of course - talk with your team!):
> A commit should be a meaning section.

- reformating is not a meaning section (suggestion: use auto formatting tools like [pre-commit hooks](https://pre-commit.com/))
- documentation **is not** a meaning section:
  - inline comment to explain unexpected code/behaviour, similar
  - doc strings while working on a new feature
- documentation **is** a meaning section:
  - rework (correct insufficient) docs on inventory feature/code

Rebase workflow might cause trouble when used artless in a team (*remote* repo).

Some advise to circumnavigate possibly appearing icebergs:

- Avoid workflows that incorporate [force pulls](https://www.freecodecamp.org/news/git-pull-force-how-to-overwrite-local-changes-with-git/).
- After a rebase you need to force push the branch to the remote. Be sure to either 
  - **work exclusively** on that branch or
  - **talk to participans** to coordinate the force push or
  - use `--force-with-lease` option when [force pushing](https://git-scm.com/docs/git-push)
- Don't touch the **main branch**. Try to get the history nice & clean before the *feature* finds its way into the *main*.
- In case you have a real good reason to mangle with the *main*:
  - don't mangle with the main ([golden rule](https://www.atlassian.com/git/tutorials/merging-vs-rebasing))
  - talk to your team find a good time to do it (a day before release might not be the time to do it)
  - inform everyone to get the new *main* and align (rebase?) their local stuff

Be sure that your git remote server follows reasonable backup plans. Quick reminder: *git* is **not a backup tool**.

### HowTo: Undo rebase

#### Using ORIG_HEAD (Simplest)

When you perform a rebase, Git saves the previous state in ORIG_HEAD:

```
git reset --hard ORIG_HEAD
```
This works only for your most recent rebase operation.

#### Using reflog

1. View the reflog to find the commit before the rebase:
    ```
    git reflog
    ```
2. Look for entries before the rebase started, typically showing your branch name.
3. Reset to that commit:
    ```
    git reset --hard HEAD@{n}
    ```
    (Replace n with the appropriate number from reflog)


# Mathquiz

A few words about the this dummy program: Simple math game. Enjoy!

Run with

```
uv run mathquiz
```

or after installing the package editable

```
uv pip install -e .

mathquiz
```
