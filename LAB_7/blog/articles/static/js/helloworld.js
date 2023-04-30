var groupmates = [
    {
        "name": "Александр",
        "surname": "Иванов",
        "group": "БСТ1702",
        "marks": [4, 3, 5]
    },
    {
        "name": "Иван",
        "surname": "Петров",
        "group": "БСТ1702",
        "marks": [4, 4, 4]
    },
    {
        "name": "Кирилл",
        "surname": "Смирнов",
        "group": "БАП1801",
        "marks": [5, 5, 5]
    }
];
//console.log(groupmates);
var rpad = function(str, length) {
    str = str.toString();
    while (str.length < length)
        str = str + ' ';
    return str;
};

var printStudents = function(students) {
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i<=students.length-1; i++){
        console.log(
            rpad(students[i]['name'], 15),
            rpad(students[i]['surname'], 15),
            rpad(students[i]['group'], 8),
            rpad(students[i]['marks'], 20)
        );
    }
    console.log('\n');
};

var filterGroup = function(students) {
    let groupName = prompt('По какой группе отфильтровать?')
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++){
        if (groupName == students[i]['group']) {
            console.log(
                rpad(students[i]['name'], 15),
                rpad(students[i]['surname'], 15),
                rpad(students[i]['group'], 8),
                rpad(students[i]['marks'], 20)
            );
        }
    }
    console.log('\n');
};

var sum = function(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    return sum;
};

var filterRating = function(students) {
    let mark = prompt('Больше какой средней оценки отфильтровать?')
    console.log(
        rpad("Имя", 15),
        rpad("Фамилия", 15),
        rpad("Группа", 8),
        rpad("Оценки", 20)
    );
    for (var i = 0; i < students.length; i++){
        var sumArr = sum(students[i]['marks']);
        var lengthArr = students[i]['marks'].length;
        if (mark <= sumArr/lengthArr) {
            console.log(
                rpad(students[i]['name'], 15),
                rpad(students[i]['surname'], 15),
                rpad(students[i]['group'], 8),
                rpad(students[i]['marks'], 20)
            );
        }
    }
    console.log('\n');
};

//filterRating(groupmates);
//filterGroup(groupmates);
//printStudents(groupmates);
