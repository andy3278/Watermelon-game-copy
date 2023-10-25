let balls = [];
let nextBall;
let nextColor;
let black = [0,0,0]
let white = [255,255,255]
let red = [255,0,0]
let orange = [255,165,0]
let yellow = [255,255,0]
let green  = [0 , 255 , 0]
let blue = [0,0,255]
let thistle = [255, 0, 255]
let hot_pink = [255, 105, 180]
let purple = [128, 0, 128]

let colorOrder = [white, red, orange,yellow, green, blue, thistle, hot_pink, purple];
let radiusOrder = [10, 15, 22, 34, 40, 52, 68, 71, 85];
let skewedProbability = [0.7, 0.1, 0.05, 0.08, 0.04, 0.02, 0.01, 0, 0];

function setup() {
    createCanvas(600, 800);
    let index = randomIndex(skewedProbability);
    nextColor = colorOrder[index];
    nextRadius = radiusOrder[index];
    nextBall = new Ball(mouseX, mouseY, nextColor, nextRadius);
}

function draw() {
    background(0);

    // Set stroke color
    stroke(255,255,255);

    // Draw box
    line(40, 40, 40, 560);
    line(40, 560, 560, 560);
    line(560, 560, 560, 40);

    // Draw balls
    for (let ball of balls) {
        ball.move();
        ball.display();
    }

    // Draw next ball at mouse position
    nextBall.x = mouseX;
    nextBall.y = mouseY;
    nextBall.display();
}

function mousePressed() {
    if (mouseX > 40 && mouseX < 560 && mouseY < 40) {
        balls.push(new Ball(mouseX, mouseY, nextColor, nextRadius));
        let index = randomIndex(skewedProbability);
        nextColor = colorOrder[index];
        nextRadius = radiusOrder[index];
        nextBall = new Ball(mouseX, mouseY, nextColor, nextRadius);
    }
}

function randomIndex(probabilities) {
    let sum = probabilities.reduce((a, b) => a + b, 0);
    let rand = random(sum);
    let cumulative = 0.0;
    for (let i = 0; i < probabilities.length; i++) {
        cumulative += probabilities[i];
        if (rand < cumulative) {
            return i;
        }
    }
    return probabilities.length - 1;
}

class Ball {
    constructor(x, y, color, radius) {
        this.x = x;
        this.y = y;
        this.r = color[0];
        this.g = color[1];
        this.b = color[2];
        this.radius = radius;
        this.velocity = 10
    }

    move() {
        // Add your ball movement logic here
        if (this.y + this.radius < 560) {
            this.y += this.velocity
        }
    }

    display() {
        fill(this.r, this.g, this.b);
        circle(this.x, this.y, 2 * this.radius);
        noStroke()
    }
}
