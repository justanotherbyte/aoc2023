use std::{fs, collections::HashMap, ops::Range};

use regex::Regex;
use indicatif::ProgressBar;

fn open_input() -> Vec<String> {
    let contents = fs::read_to_string("../input.txt")
        .expect("Failed to read input.txt");

    let lines: Vec<&str> = contents.split('\n').collect();
    let mut out = vec![];
    for line in lines {
        let owned = line.to_string();
        out.push(owned)
    }
    out
}

fn get_numbers_from_line(line: &str) -> Vec<u64> {
    let re = Regex::new(r"\d+").unwrap();
    let mut nums = vec![];
    let matches: Vec<_> = re.find_iter(line).map(|m| m.as_str()).collect();

    for m in matches {
        let num: u64 = m.parse().unwrap();
        nums.push(num);
    }

    nums
}

fn get_category_map_name(line: &str) -> Option<String> {
    let re = Regex::new(r"^(.*?)(map:)").unwrap();
    let mat = re.is_match(line);
    if mat {
        let cmn = line.replace(" map:", "");
        Some(cmn)
    } else {
        None
    }
}

fn expand_nums(nums: (u64, u64, u64)) -> Vec<(u64, u64)> {
    let (drs, srs, rl) = nums;
    let (mind, maxd) = (drs, drs + rl);
    let (mins, maxs) = (srs, srs + rl);
    vec![(mind, maxd), (mins, maxs)]
}

fn calc_locs(pbar: &ProgressBar, sn: Range<u64>, categories: &Vec<String>, maps: &HashMap<String, Vec<Vec<(u64, u64)>>>, locs: &mut Vec<u64>) {
    for seed_num in sn {
        let (mut dest, _) = (seed_num, seed_num);
        
        for category in categories {
            let lines = maps.get(category).unwrap();
            for line in lines {
                let (mind, _) = line[0];
                let (mins, maxs) = line[1];

                if (mins..maxs).contains(&dest) {
                    let diff = (dest.clone()) - mins;
                    dest = diff + mind;
                    break;
                }
            }
        }
        locs.push(dest.clone());
        pbar.inc(1);
    }
}

fn main() {
    let lines = open_input();
    let mut categories = vec![];
    let mut category_maps: HashMap<String, Vec<Vec<(u64, u64)>>> = HashMap::new();

    let mut last_category_map = String::new();
    let mut num_rows = vec![];
    for (idx, line) in lines.iter().enumerate() {
        if line == "\n" || idx == 0 || line.is_empty() {
            continue
        }

        let category_map_name = get_category_map_name(line);
        if let Some(category_map_name) = category_map_name {
            category_maps.insert(last_category_map, num_rows.clone());
            num_rows.clear();
            let cloned_cm_name = category_map_name.clone();
            last_category_map = category_map_name;
            categories.push(cloned_cm_name);
        } else {
            let nums = get_numbers_from_line(line);
            let nt = (nums[0], nums[1], nums[2]);
            num_rows.push(expand_nums(nt));
        }

        if idx == (lines.len() - 1) {
            category_maps.insert(last_category_map, num_rows.clone());
            break;
        }
    }

    category_maps.remove("");

    let seed_nums = get_numbers_from_line(&lines[0]);

    let mut locs = vec![];
    let mut new_seed_nums = vec![];
    let mut new_seed_sizes = vec![];

    let mut flag = true;
    for seed in seed_nums {
        if flag {
            new_seed_nums.push(seed);
            flag = false;
        } else {
            new_seed_sizes.push(seed);
            flag = true;
        }
    }
    
    let seed_count: u64 = new_seed_sizes.iter().sum();
    let progress_bar = ProgressBar::new(seed_count);

    for (idx, seed) in new_seed_nums.iter().enumerate() {
        let size = new_seed_sizes[idx];
        let r = (*seed)..(seed + size);
        calc_locs(&progress_bar, r, &categories, &category_maps, &mut locs);
    }

    progress_bar.finish();
    let min_dest = locs.iter().min().unwrap();
    println!("{min_dest:?}");
}
