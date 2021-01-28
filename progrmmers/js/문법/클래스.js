// js에서 클래스 사용
class Animal {
    constructor(type, name, sound) {
      this.type = type;
      this.name = name;
      this.sound = sound;
    }
  }
  
  class Dog extends Animal {
    constructor(name, sound) {
      super('개', name, sound);
    }
  }
  
  class Cat extends Animal {
    constructor(name, sound) {
      super('고양이', name, sound);
    }
  }
  
  const dog = new Dog('멍멍이', '멍멍');
  const dog2 = new Dog('왈왈이', '왈왈');
  const cat = new Cat('야옹이', '야옹');
  const cat2 = new Cat('냐옹이', '냐옹');
  
  dog.say();
  dog2.say();
  cat.say();
  cat2.say();