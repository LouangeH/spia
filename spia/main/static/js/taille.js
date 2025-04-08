const steps = document.querySelectorAll(".step");
let currentStep = 0;

document.querySelectorAll(".next-step").forEach(button => {
    button.addEventListener("click", () => {
        steps[currentStep].classList.add("d-none");
        currentStep++;
        steps[currentStep].classList.remove("d-none");
    });
});

document.querySelectorAll(".prev-step").forEach(button => {
    button.addEventListener("click", () => {
        steps[currentStep].classList.add("d-none");
        currentStep--;
        steps[currentStep].classList.remove("d-none");
    });
});

document.querySelectorAll(".file-input").forEach(input => {
    input.addEventListener("change", (event) => {
        if (event.target.files[0].size > 200000) {
            alert("File size must be under 200KB");
            event.target.value = "";
        }
    });
});