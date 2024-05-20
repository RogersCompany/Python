/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

var twoSum = function(nums, target) {
    const map1 = new Map();
    for (let i = 0; i < nums.length; i++)
    {
        const res = target - nums[i];
        if (map1.has(res))
            return [map1.get(res), i]
        
        map1.set(nums[i], i)
    }
    return [];
};