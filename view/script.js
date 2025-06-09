// Theme handling
const prefersDark = window.matchMedia('(prefers-color-scheme: dark)');
const currentTheme = localStorage.getItem('theme');

if (currentTheme === 'dark') {
    document.documentElement.setAttribute('data-theme', 'dark');
    document.getElementById('checkbox').checked = true;
} else if (currentTheme === 'light') {
    document.documentElement.setAttribute('data-theme', 'light');
    document.getElementById('checkbox').checked = false;
} else {
    // Use system preference
    if (prefersDark.matches) {
        document.documentElement.setAttribute('data-theme', 'dark');
        document.getElementById('checkbox').checked = true;
    }
}

function switchTheme(e) {
    if (e.target.checked) {
        document.documentElement.setAttribute('data-theme', 'dark');
        localStorage.setItem('theme', 'dark');
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        localStorage.setItem('theme', 'light');
    }    
}

document.getElementById('checkbox').addEventListener('change', switchTheme);

// LeetCode Stats
async function fetchLeetCodeStats() {
    try {
        const username = 'AmanKadam-16';
        const response = await fetch(`https://leetcode-stats-api.herokuapp.com/${username}`);
        const data = await response.json();

        // Update total solved and general stats
        document.querySelector('.total .stat-number').textContent = data.totalSolved || '0';
        document.querySelector('.acceptance-rate').textContent = `${data.acceptanceRate || '0'}%`;
        document.querySelector('.user-rank').textContent = data.ranking || '0';

        // Update difficulty breakdown
        document.querySelector('.difficulty.easy .value').textContent = data.easySolved || '0';
        document.querySelector('.difficulty.medium .value').textContent = data.mediumSolved || '0';
        document.querySelector('.difficulty.hard .value').textContent = data.hardSolved || '0';

        // Update progress bar
        const totalProblems = data.totalQuestions || 100;
        const progressWidth = (data.totalSolved / totalProblems) * 100;
        document.querySelector('.progress-bars::before').style.width = `${progressWidth}%`;

        // Get streak from localStorage or initialize
        let streak = parseInt(localStorage.getItem('leetcodeStreak')) || 0;
        let lastSolveDate = localStorage.getItem('lastSolveDate');
        const today = new Date().toDateString();
        
        if (lastSolveDate !== today && data.totalSolved > parseInt(localStorage.getItem('lastTotalSolved') || '0')) {
            streak++;
            localStorage.setItem('leetcodeStreak', streak);
            localStorage.setItem('lastSolveDate', today);
            localStorage.setItem('lastTotalSolved', data.totalSolved);
        }
        
        document.querySelector('.streak .stat-number').textContent = streak;
        document.querySelector('.submission-count').textContent = data.totalSubmissions || '0';

        // Update contribution stats
        document.querySelector('.points').textContent = data.contributionPoints || '0';
        document.querySelector('.reputation').textContent = data.reputation || '0';

    } catch (error) {
        console.error('Error fetching LeetCode stats:', error);
    }
}

// Update stats initially and every 30 minutes
fetchLeetCodeStats();
setInterval(fetchLeetCodeStats, 30 * 60 * 1000);
