'use strict';

var arrows = document.querySelector('.quantity').querySelectorAll('.fa');

var handleChange = function handleChange(elem) {
  var qt = document.querySelector('#qt');
  var total = document.querySelector('#price');
  var value = parseInt(qt.innerText);
  var classArr = Array.from(elem.classList);
  if (/right/gi.test(classArr)) {
    if (value != 9) value++;else alert('Watch out! We\'ve got a badass over here!');
  } else {
    if (value != 1) value--;else alert('Watch out! We\'ve got a badass over here!');
  }
  qt.innerText = value;
  total.innerText = '$' + value * 320;
};

var product = document.querySelector('.product');

var moveBox = function moveBox(val) {
  product.style.mozTransform = product.style.msTransform = product.style.webkitTransform = product.style.transform = 'translateX(' + val + 'px)';
};

var back = document.querySelector('.back');

var spring = new rebound.SpringSystem();

var animation = spring.createSpring(60, 3);

animation.addListener({
  onSpringUpdate: function onSpringUpdate(spring) {
    var current = spring.getCurrentValue();
    if (current > 1) spring.setEndValue(0);
    var val = rebound.MathUtil.mapValueInRange(current, 0, 1, 0, 20);
    moveBox(val);
  }
});

back.addEventListener('click', function () {
  animation.setEndValue(1);
});

var arrArr = Array.from(arrows);

arrArr.forEach(function (elem) {
  elem.addEventListener('click', function () {
    handleChange(elem);
  });
});
