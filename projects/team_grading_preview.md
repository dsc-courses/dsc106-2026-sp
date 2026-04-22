---
layout: page
title: 'Team Grading Preview'
parent: '📝 Projects'
nav_order: 8
---

# Team Grading Preview

This preview shows how team grading adjustments are calculated from team-member ratings.

- **Indiv. Avg.** is the average rating a student receives from all team members.
- **Team Avg.** is the average of all ratings for the whole team.
- **Grade adjustment** is a multiplier applied to the team's project grade, not a number added to the team average. It is calculated as `Indiv. Avg. / Team Avg.`. For example, a ratio of `0.75` is shown as `-25%`, while a ratio of `1.05` is shown as `+5%`.
- Positive adjustments are capped at `1.05`, or +5%.

Example 1: suppose a team receives 90% on the project and everyone rates everyone as 100.

- Each student has an individual average of 100 and the team average is also 100.
- Each student's grade adjustment is `100 / 100 = 1.00`, or +0%.
- Each student's final grade is `90 * 1.00 = 90`.

Example 2: suppose a 3-person team has a project grade of 90, everyone rates everyone as 100, except team member 1 rates team member 2 as 0.

- Team member 1 has an individual average of 100, a team average of 88.9, and a capped adjustment of +5%, so their final grade is `90 * 1.05 = 94.5`.
- Team member 2 has an individual average of 66.7 and an adjustment of -25%, so their final grade is `90 * 0.75 = 67.5`.

<div id="team-grading-tool" class="team-grading-preview">
  <template id="rating-template">
    <select class="rating-select" aria-label="Team rating">
      <option value="100">100</option>
      <option value="90">90</option>
      <option value="60">60</option>
      <option value="40">40</option>
      <option value="0">0</option>
    </select>
  </template>

  <div class="team-grading-controls">
    <fieldset class="team-size-control">
      <legend>Team members:</legend>
      <label>
        <input type="radio" name="team-size" value="3">
        3
      </label>
      <label>
        <input type="radio" name="team-size" value="4" checked>
        4
      </label>
    </fieldset>

    <p class="rating-legend">
      Ratings: 100 = Good team citizen, 90 = Needs improvement, 60 = Deficient, 40 = Unsatisfactory, 0 = No show.
    </p>
  </div>

  <div class="team-grading-table-wrap">
    <table class="team-grading-table">
      <thead>
        <tr>
          <th scope="col"></th>
          <th scope="col">Rater 1</th>
          <th scope="col">Rater 2</th>
          <th scope="col">Rater 3</th>
          <th scope="col" data-member="4">Rater 4</th>
          <th scope="col">Indiv. Avg.</th>
          <th scope="col">Team Avg.</th>
          <th scope="col">Adjustment</th>
        </tr>
      </thead>
      <tbody>
        {% for rated in (1..4) %}
        <tr data-member="{{ rated }}">
          <th scope="row">Member {{ rated }}</th>
          {% for rater in (1..4) %}
          <td data-member="{{ rater }}"><span data-rating-cell data-rated="{{ rated }}" data-rater="{{ rater }}"></span></td>
          {% endfor %}
          <td><span data-individual-average="{{ rated }}"></span></td>
          <td><span data-team-average="{{ rated }}"></span></td>
          <td><span data-adjustment="{{ rated }}"></span></td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
  </div>
</div>

<style>
  .team-grading-preview {
    margin-top: 1rem;
  }

  .team-grading-controls {
    margin-bottom: 1rem;
  }

  .team-grading-preview .team-size-control {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 0.5rem;
    padding: 0;
    border: 0;
    font-weight: 600;
  }

  .team-grading-preview .team-size-control legend {
    padding: 0;
  }

  .team-grading-preview .team-size-control label {
    display: inline-flex;
    align-items: center;
    gap: 0.25rem;
  }

  .team-grading-preview .rating-legend {
    margin: 0;
  }

  .team-grading-preview select {
    max-width: 100%;
  }

  .team-grading-preview .rating-select {
    min-width: 3.35rem;
  }

  .team-grading-table-wrap {
    overflow-x: auto;
  }

  .team-grading-table-wrap .table-wrapper {
    min-width: 0;
  }

  .team-grading-table {
    width: 100%;
    min-width: 0;
    border-collapse: collapse;
  }

  .team-grading-table th,
  .team-grading-table td {
    border: 1px solid #111;
    min-width: 0;
    padding: 0.25rem 0.35rem;
    vertical-align: middle;
    white-space: nowrap;
  }

  .team-grading-table th {
    font-weight: 700;
  }

  .team-grading-table [hidden] {
    display: none;
  }
</style>

<script>
  (function () {
    const maxTeamSize = 4;
    const preview = document.getElementById("team-grading-tool");
    const teamSizeInputs = preview.querySelectorAll('input[name="team-size"]');
    const template = document.getElementById("rating-template");

    if (!preview || teamSizeInputs.length === 0 || !template) {
      return;
    }

    function teamSize() {
      return parseInt(preview.querySelector('input[name="team-size"]:checked').value, 10);
    }

    function ratingCell(rated, rater) {
      return preview.querySelector(
        `[data-rating-cell][data-rated="${rated}"][data-rater="${rater}"]`
      );
    }

    function populateRatings() {
      preview.querySelectorAll("[data-rating-cell]").forEach((cell) => {
        const select = template.content.firstElementChild.cloneNode(true);
        select.addEventListener("change", update);
        cell.append(select);
      });
    }

    function setMemberVisibility() {
      const size = teamSize();

      for (let member = 1; member <= maxTeamSize; member += 1) {
        const hidden = member > size;
        preview.querySelectorAll(`[data-member="${member}"]`).forEach((node) => {
          node.hidden = hidden;
        });
      }
    }

    function update() {
      const size = teamSize();
      const ratings = Array.from({ length: size }, () =>
        Array.from({ length: size }, () => 0)
      );
      let total = 0;

      for (let rater = 1; rater <= size; rater += 1) {
        for (let rated = 1; rated <= size; rated += 1) {
          const select = ratingCell(rated, rater).querySelector("select");
          const score = parseInt(select.value, 10);
          ratings[rater - 1][rated - 1] = score;
          total += score;
        }
      }

      const teamAverage = total / size / size;

      for (let rated = 1; rated <= size; rated += 1) {
        let individualTotal = 0;

        for (let rater = 1; rater <= size; rater += 1) {
          individualTotal += ratings[rater - 1][rated - 1];
        }

        const individualAverage = individualTotal / size;
        const adjustment = Math.min(1.05, individualAverage / teamAverage);
        const adjustmentPercent = Math.round((adjustment - 1) * 100);

        preview.querySelector(`[data-individual-average="${rated}"]`).textContent =
          individualAverage.toFixed(1);
        preview.querySelector(`[data-team-average="${rated}"]`).textContent =
          teamAverage.toFixed(1);
        preview.querySelector(`[data-adjustment="${rated}"]`).textContent =
          `${adjustmentPercent >= 0 ? "+" : ""}${adjustmentPercent}%`;
      }
    }

    function updateTeamSize() {
      setMemberVisibility();
      update();
    }

    populateRatings();
    teamSizeInputs.forEach((input) => input.addEventListener("change", updateTeamSize));
    updateTeamSize();
  })();
</script>
