
    return rest.reduce((acc, current) => acc + current, 0);
}
const res = sum(1, 2, 3, 4, 5, 6);
console.log(res); // 21