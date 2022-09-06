#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w <= 0) || (h <= 0)) {
      return this;
    }
    if ((typeof w === 'undefined') || (typeof h === 'undefined')) {
      return this;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}

class Square extends Rectangle {
  constructor (size) {
    super();
    this.size = size;
  }

  print () {
    for (let i = 0; i < this.size; i++) {
      console.log('X'.repeat(this.size));
    }
  }

  double () {
    this.size = this.size * 2;
  }
}

module.exports = Square;
