const rectangles = document.querySelectorAll('.rectangle'); // gets all of the rectangles and stores them
const gridContainer = document.getElementById('grid-container');
const submitButton = document.getElementById('submit-button'); // stores submit button
const deselectButton = document.getElementById('deselect-button');

let selectedCount = 0;
let numAttempts = 0; 

let correctCategories = 0;
let mistakeCount = 0; 

let categoryIndex = 1;

const mistakeCircles = document.querySelectorAll('.circle');

var m1 = document.getElementById('circle4');
var m2 = document.getElementById('circle3');
var m3 = document.getElementById('circle2');
var m4 = document.getElementById('circle1');

rectangles.forEach(rectangle => {
    rectangle.addEventListener('click', () => {
        const isSelected = rectangle.getAttribute('data-selected') === 'true'; // determines if rectangle selected

        // allows selection of rectangle item if not already selected and there aren't 4 selected already
        if (!isSelected && selectedCount < 4) {
            rectangle.setAttribute('data-selected', 'true'); // makes it a selected rectangle
            rectangle.classList.add('selected'); // adds to list of selected rectangles
            selectedCount++;
            updateSubmitButton(); // activates submit button if 4 selected
        } 
        // handles deselectingan already selected item
        else if (isSelected) {
            rectangle.setAttribute('data-selected', 'false'); // removes selected attribute by making it false
            rectangle.classList.remove('selected'); // removes from chosen list and decrements
            selectedCount--;
            updateSubmitButton(); // if under 4 are selected now, it deactivates submit button
        }
    });
});

// this activates the submit button where 4 items are selected
function updateSubmitButton() {
    if (selectedCount > 0) {
        deselectButton.removeAttribute('disabled');
    }
    else {
        deselectButton.setAttribute('disabled', 'disabled');
    }
    if (selectedCount === 4) {
        submitButton.removeAttribute('disabled'); // enables when 4 selected
    } 
    else {
        submitButton.setAttribute('disabled', 'disabled'); // disables button
    }
}

function updateMistakeCounter() {
    if (mistakeCount == 1) {
        doMistakeAnimation(m1);
    }
    if (mistakeCount == 2) {
        doMistakeAnimation(m2);
    }
    if (mistakeCount == 3) {
        doMistakeAnimation(m3);
    }
    if (mistakeCount == 4) {
        doMistakeAnimation(m4);
        // gameLost(); handles when they exceed mistake count
    }
}

function doMistakeAnimation(m) {
    animationRandom = Math.random();
    if (animationRandom < 0.5) {
        m.classList.add('hopOff');
    }
    else {
        m.classList.add('popFade');
    }

}

// event listener for clicking submit button
// pre: there are 4 items selected and the button is not disabled
document.getElementById('submit-button').addEventListener('click', () => {
    triggerAnimation();
});

let numAnimationsRemoved = 0;
let numShakeAnimationsRemoved = 0;
// adds animation end event listener for reach rectangle
document.querySelectorAll('.rectangle').forEach(rectangle => {
    rectangle.addEventListener('animationend', () => {
        rectangle.classList.remove('jump-animation'); // removes the jump animation from rectangle
        console.log("oi");
        numAnimationsRemoved++;
        if (numAnimationsRemoved == 4) {
            console.log("checking")
            checkSelection();
            numAnimationsRemoved = 0;
        }
    });

    rectangle.addEventListener('animationend', () => {
        if (rectangle.classList.contains('shake-animation')) {
            numShakeAnimationsRemoved++;
            if (numShakeAnimationsRemoved === document.querySelectorAll('.selected'),length) {
                checkSelection();
                numShakeAnimationsRemoved = 0;
            }
        }
    })
});

// makes them do the jump animation after submit button hit
function triggerAnimation() {
    const selectedRectangles = document.querySelectorAll('.selected'); // gathers all selected rectangles
    selectedRectangles.forEach((rectangle, index) => {
        setTimeout(() => {
            rectangle.classList.add('jump-animation');
            console.log("Jump")
        }, index * 100); // Delay each jump animation by 100ms
    });
}

// checks if the selected items belong to the same category or not
function checkSelection() {
    console.log("checking selection...")
    const selectedCategories = new Set(); // makes empty set for the different categories
    const selectedRectangles = document.querySelectorAll('.selected'); // gathers all selected items

    selectedRectangles.forEach(rectangle => {
        selectedCategories.add(rectangle.dataset.category);
    });

    // when the submission is correct
    if (selectedCategories.size === 1) { // means they all are in same category
        console.log('Correct selection');
        correctCategories++;
        const category = selectedRectangles[0].dataset.category;
        moveCorrectItemsToTopRow(selectedRectangles);
        combineItemsIntoOneRectangle(category, selectedRectangles);
    } 
    // when submission is incorrect
    else {
        console.log('Incorrect selection');
        shakeAllRectangles();
        mistakeCount++;
        updateMistakeCounter();
    }
    // Update the display to show the current mistake count
    //document.getElementById('mistake-count').textContent = 'Mistakes: ' + mistakeCount;
}

function moveCorrectItemsToTopRow(selectedRectangles) {
    const topRowRectangles = document.querySelectorAll('.grid-container > .rectangle:nth-child(-n+4)');

    selectedRectangles.forEach((rectangle, index) => {
        const targetPosition = topRowRectangles[index].getBoundingClientRect();
        const currentPosition = rectangle.getBoundingClientRect();

        const deltaX = targetPosition.left - currentPosition.left;
        const deltaY = targetPosition.top - currentPosition.top;

        rectangle.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
    });
}


function combineItemsIntoOneRectangle(category, selectedRectangles) {
    // Create a new combined rectangle
    const combinedRectangle = document.createElement('div');
    if (correctCategories == 1) {
        combinedRectangle.classList.add('completed-category-1');
    }
    else if (correctCategories == 2) {
        combinedRectangle.classList.add('completed-category-2');
    }
    else if (correctCategories == 3) {
        combinedRectangle.classList.add('completed-category-3');
    }
    else if (correctCategories == 4) {
        combinedRectangle.classList.add('completed-category-4');
    }
    combinedRectangle.style.gridRow = categoryIndex;
    combinedRectangle.style.gridColumn = '1 / span 4';

    // Set the content to display the category name and item names
    combinedRectangle.innerHTML = `<div class="category">${category}</div>`;

    // Append the combined rectangle to the grid container
    document.getElementById('grid-container').appendChild(combinedRectangle);

    // Remove the selected rectangles from the grid
    selectedRectangles.forEach(rectangle => {
        rectangle.remove();
    });
    
    categoryIndex++;
    selectedCount = 0;
    updateSubmitButton();

}

// shakes the rectangles
async function shakeAllRectangles() {
    // Add the shake-animation class to start the animation
    document.querySelectorAll('.selected').forEach(rectangle => {
        rectangle.classList.add('shake-animation');
    });

    // Wait for the shake animation to complete
    await addPause(450);

    // Remove the shake-animation class to reset the animation for subsequent submissions
    document.querySelectorAll('.selected').forEach(rectangle => {
        rectangle.classList.remove('shake-animation');
    });
}

function addPause(duration) {
    return new Promise(resolve => setTimeout(resolve, duration));
}

document.getElementById('deselect-button').addEventListener('click', () => {
    deselectAllItems();
});

// deselects all current selected items
function deselectAllItems() {
    document.querySelectorAll('.selected').forEach(rectangle => {
        rectangle.classList.remove('selected'); // removes from selected list
        rectangle.setAttribute('data-selected', 'false');  // removes selected state from item
        submitButton.setAttribute('disabled', 'disabled');
        selectedCount = 0; 
        updateSubmitButton(); // resets submit button
    });
}

document.getElementById('shuffle-button').addEventListener('click', shuffleAllItems);

// shuffles all of the items on the grid
function shuffleAllItems() {
    const items = Array.from(gridContainer.children);
    const shuffledItems = shuffleArray(items);

    gridContainer.innerHTML = ''; // Clear the container

    shuffledItems.forEach(item => {
        gridContainer.appendChild(item);
    });
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap elements
    }
    return array;
}

// Function to populate dates in the dropdown menu
function populateDates() {
    // Fetch dates from the server using an AJAX request
    fetch('/get_previous_dates') // Assuming '/get_previous_dates' is the Flask route to fetch dates
        .then(response => response.json())
        .then(data => {
            // Populate dates into the dropdown menu
            const dropdownContent = document.getElementById('games-dropdown-content');
            dropdownContent.innerHTML = ''; // Clear previous options
            data.forEach(date => {
                const option = document.createElement('a');
                option.textContent = date;
                dropdownContent.appendChild(option);
            });
        })
        .catch(error => {
            console.error('Error fetching dates:', error);
        });
}

// Event listener for the dropdown button
document.getElementById('previous-games-button').addEventListener('click', () => {
    // Toggle the visibility of the dropdown content
    const dropdownContent = document.getElementById('games-dropdown-content');
    dropdownContent.style.display = (dropdownContent.style.display === 'block') ? 'none' : 'block';

    // Populate dates if the dropdown content is visible
    if (dropdownContent.style.display === 'block') {
        populateDates();
    }
});
