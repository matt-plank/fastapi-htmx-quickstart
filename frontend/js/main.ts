type Person = {
  name: string;
  age: number;
  height: number;
};

const testPerson: Person = {
  name: "John",
  age: 25,
  height: 172,
};

(window as any).test = () => {
  console.log(testPerson);
};
