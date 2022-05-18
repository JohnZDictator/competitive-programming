const howSum = (targetSum, numbers) => {
    if(targetSum === 0) return [];
    if(targetSum < 0) return null;

    for(let num of numbers){
        const rem = targetSum - num;
        const remResult = howSum(rem, numbers);
        if(remResult !== null){
            return [...remResult, num];
        }
    }
    return null;
}


console.log(howSum(7, [2,3,4,7]))
console.log(howSum(7, [2,4]))