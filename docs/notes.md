# Scatterbrain Developer Notes

## 2021-01-11 18.45.00

The idea behind scatterbrain is a specialized note taking system to include features like kanban boards, timestamped tagged posts, indexing, and other cool features
while allowing me to work on my project organizational skills before my internship.
I was a bit taken aback when I realized that GitHub already had a kanban board feature,
but that is what I get for using GitLab all this time.

After a bit of investigation, the GitHub cards are incredibly rudementary and do not contain the features that I want, such as check lists and individual item due dates and flexible card layouts.  They are basically single box notes until you turn them into issues, which adds some but not all the features that I am looking for.

## 2021-01-20 15:28:41

Still setting up the framework for the project.  Getting back into the groove of setting up a project after one, not contributing for a time, and two, using cookiecutter before that.  Luckily I was using such a well documented system that I can just follow along to get it all back into my working memory.

## 2021-01-25 22:32:44

The complexity of the card system is going to take some planning.  I want for the cards to be able to have multiple check lists, which each have items that can contain a lot of data.  I might try and make a redundant unit called a task that can be a member of a board or a member of a checklist, and can itself contain check lists, due dates, events, reminders, notes, labels, and other things.  I think it would be counter productive most of the time to have a card with tasks that have tasks and so on, but it could be useful, and it would make the code reusable.  The boards could contain lists, which themselves are task entities that contain cards, that then contain check lists.  I need to do more planning.

* Team: Contains members and projects.
* Member: A user that can be assigned tasks, belongs to a team, and works on projects.
* Project: A collection of boards that belongs to a team.
* Board: A collection of lists.
* Lists: A collection of cards that functions like labels on a board.
* Cards: A task that can contain sublists, but is usually a full unit of work.
* Subtask: An item on a checklist that is a component of the task for the card.
