import fetch from 'node-fetch';

(async () => {
  // let start = new Date().getTime();

  const promises = [];

  const makeRequests = () => {
    for (let i = 0; i < 120; i++) {
      const p = fetch(`http://localhost:8000/auth/login?id=${i}`, {
        method: 'post',
        body: JSON.stringify({
          fullname: 'Dan Skrypnik',
          email: 'dynastytyan@gmail.com',
          password: '123',
        }),
        headers: {
          'Content-Type': 'application/json',
        },
      });
      promises.push(p);
    }
  };

  // setInterval(makeRequests, 500);
  makeRequests();

  const elapsing = [];

  for await (const p of promises) {
    const start = performance.now();
    const res = await p;
    const text = await res.text();

    const items = text.split(' ');
    const elapsedFromServer = items[items.length - 1];

    elapsing.push(Number(elapsedFromServer));

    const finish = performance.now() - start;
    // console.log(' elapsed:', ~~finish, 'ms', text);
  }

  // const res = await p;
  // const finish = new Date().getTime() - start;
  // console.log(await res.text(), ' elapsed: ', finish, 'ms');
  // console.log(' elapsed: ', finish, 'ms');

  const sum = (arr) => {
    return arr.reduce((prev, cur) => prev + cur);
  };

  console.log('max: ', Math.max(...elapsing));
  console.log('min: ', Math.min(...elapsing));
  console.log('avg: ', sum(elapsing) / elapsing.length);

  console.log(elapsing.reverse());
})();
