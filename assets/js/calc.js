document.getElementById("calorieForm").addEventListener("submit", function(e) {
    e.preventDefault();

    // Get form values
    const gender = document.getElementById("gender").value;
    const weight = parseFloat(document.getElementById("weight").value);
    const height = parseFloat(document.getElementById("height").value);
    const age = parseInt(document.getElementById("age").value);
    const goal = document.getElementById("goal").value;
    const activity = document.getElementById("activity").value;

    // Validation
    if (!gender || !weight || !height || !age || !goal || !activity) {
        alert("Please fill out all fields correctly.");
        return;
    }

    // Calculate BMR
    let bmr;
    if (gender === "male") {
        bmr = 10 * weight + 6.25 * height - 5 * age + 5;
    } else {
        bmr = 10 * weight + 6.25 * height - 5 * age - 161;
    }

    // Adjust BMR based on activity
    const activityMultiplier = {
        sedentary: 1.2,
        light: 1.375,
        moderate: 1.55,
        active: 1.725,
    };

    const calorieNeeds = bmr * activityMultiplier[activity];

    // Adjust based on goal
    let finalCalories;
    if (goal === "lose") {
        finalCalories = calorieNeeds - 500;
    } else if (goal === "gain") {
        finalCalories = calorieNeeds + 500;
    } else {
        finalCalories = calorieNeeds;
    }

    // Display result
    document.getElementById("result").innerHTML = `Your daily calorie needs: <strong>${Math.round(
      finalCalories
    )} kcal</strong>`;
});