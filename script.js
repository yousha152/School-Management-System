let students = {};
let teachers = {};

document.addEventListener("DOMContentLoaded", () => {
    setupNavigation();
    setupForms();
});

function setupNavigation() {
    const buttons = document.querySelectorAll(".nav-btn");
    buttons.forEach(btn => {
        btn.addEventListener("click", () => {
            buttons.forEach(b => b.classList.remove("active"));
            document.querySelectorAll(".tab-content").forEach(c => c.classList.remove("active"));
            
            btn.classList.add("active");
            const tabId = btn.getAttribute("data-tab");
            document.getElementById(tabId).classList.add("active");
            document.getElementById("pageTitle").innerText = btn.innerText;
        });
    });
}

function updateStudentDropdowns() {
    const selects = ["attStudentSelect", "marksStudentSelect", "feeStudentSelect"];
    selects.forEach(id => {
        const el = document.getElementById(id);
        el.innerHTML = '<option value="">Select Student</option>';
        Object.keys(students).forEach(id => {
            el.innerHTML += `<option value="${id}">${id} - ${students[id].info.name}</option>`;
        });
    });
}

function setupForms() {
    // Add Student
    document.getElementById("studentForm").addEventListener("submit", (e) => {
        e.preventDefault();
        const id = document.getElementById("stId").value.trim().toUpperCase();
        if (students[id]) return alert("Student ID already exists!");

        students[id] = {
            info: {
                name: document.getElementById("stName").value.trim(),
                age: document.getElementById("stAge").value,
                gender: document.getElementById("stGender").value,
                class: document.getElementById("stClass").value,
                section: document.getElementById("stSection").value,
                father: document.getElementById("stFather").value,
                contact: document.getElementById("stContact").value
            },
            attendance: { present: 0, total: 0 },
            marks: {},
            fees: { remaining: 0 }
        };

        renderStudents();
        updateStudentDropdowns();
        e.target.reset();
    });

    // Add Teacher
    document.getElementById("teacherForm").addEventListener("submit", (e) => {
        e.preventDefault();
        const id = document.getElementById("tId").value.trim().toUpperCase();
        if (teachers[id]) return alert("Teacher ID exists!");

        teachers[id] = {
            name: document.getElementById("tName").value.trim(),
            subject: document.getElementById("tSubject").value,
            contact: document.getElementById("tContact").value,
            class: document.getElementById("tClass").value
        };

        renderTeachers();
        e.target.reset();
    });
}

function renderStudents() {
    const tbody = document.getElementById("studentTableBody");
    tbody.innerHTML = "";
    Object.keys(students).forEach(id => {
        const s = students[id].info;
        tbody.innerHTML += `<tr><td>${id}</td><td>${s.name}</td><td>${s.class}</td><td>${s.section}</td><td>${s.contact}</td></tr>`;
    });
    document.getElementById("totalStudentsCount").innerText = Object.keys(students).length;
}

function renderTeachers() {
    const tbody = document.getElementById("teacherTableBody");
    tbody.innerHTML = "";
    Object.keys(teachers).forEach(id => {
        const t = teachers[id];
        tbody.innerHTML += `<tr><td>${id}</td><td>${t.name}</td><td>${t.subject}</td><td>${t.class}</td><td>${t.contact}</td></tr>`;
    });
    document.getElementById("totalTeachersCount").innerText = Object.keys(teachers).length;
}