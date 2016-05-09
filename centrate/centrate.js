//(function () {
/**
 * generate all permutations p(n, k). Method is inefficient replace it with a serious combinatorics function
 * generates strings
 */
function perm_idx(n, k) {
    var a, r;
    if (k === 1) {
        r = [];
        for (a = 0; a < n; a++) {
            r.push(a + '');
        }
        return r;
    } else {
        var perm_c = perm_idx(n, k - 1);
        r = [];
        for (a = 0; a < n; a++) {
            for (var i = 0; i < perm_c.length; i++) {
                var cp = perm_c[i];
                if (cp.indexOf(a) === -1) {
                    r.push(a + cp);
                }
            }
        }
        return r;
    }
}

// use strings for convenience, they have == and printing while [] are bad at this
var INITIAL_SET = perm_idx(10, 4);
var ALL_ANSWERS = [
    '00',
    '10', '01',
    '20', '11', '02',
    '30', '21', '12', '03',
    '40', '22', '13', '04'];


function evaluate(nr, question) {
    var centr = 0;
    var necentr = 0;
    for (var i = 0; i < question.length; i++) {
        var a = question[i];
        var j = nr.indexOf(a);
        if (j !== -1) {
            if (j == i) {
                centr += 1;
            } else {
                necentr += 1;
            }
        }
    }
    return centr + '' + necentr;
}

function restrict_solutions(solutions, question, a_c, a_nc) {
    function number_fits_question(n) {
        return evaluate(n, question) == a_c + '' + a_nc;
    }

    return solutions.filter(function (s) {
        return number_fits_question(s)
    });
}

/**
 * A set of solutions is given.
 * The given question will have possible different answers for each solution in the set.
 * Returns the distribution answer->subset of solutions giving this answer
 */
function question_distribution(solutions, question) {
    var dist = {};
    for (var i = 0; i < solutions.length; i++) {
        var ev = evaluate(solutions[i], question);
        if (ev in dist) {
            dist[ev] += 1;
        } else {
            dist[ev] = 1
        }
    }
    return dist;
}


function min_distribution(solutions) {
    var new_q = [];
    var min_score = 1000;
    // a dumb but reasonable way to reduce the search space is to random sample some of the possible questions
    for (var i = 0; i < INITIAL_SET.length; i++) {
        var q = INITIAL_SET[i];

        var dist = question_distribution(solutions, q);

        var score = 0;
        for (var k in dist) {
            var value = dist[k];
            if (value > score) {
                score = value;
            }
        }

        if (score < min_score) {
            min_score = score;
            new_q = q;
        }
    }
    console.log('at score' + min_score + 'found' + new_q);
    return new_q;
}

var PRECOM_1234 = {
    '01': '0156', '12': '0235', '00': '0567',
    '30': '0235', '04': '0342', '21': '0135',
    '02': '0342', '20': '0135', '13': '0123',
    '22': '0123', '10': '0235', '03': '0125',
    '11': '0235', '40': '0123'
};


function Solver() {
    this.solutions = INITIAL_SET;
    this.new_q = '1234';
    this.step = 0;
}


Solver.prototype.get_question = function () {
    if (this.step > 1) {
        this.new_q = min_distribution(this.solutions);
    }
    this.step += 1;
    return this.new_q;
};

Solver.prototype.send_answer = function (c, nc) {
    this.solutions = restrict_solutions(this.solutions, this.new_q, c, nc);
    if (this.step == 1) {
        this.new_q = PRECOM_1234[c + '' + nc];
    }
    var r;
    if (this.solutions.length === 1) {
        r = 'success';
    } else if (this.solutions.length === 0) {
        r = 'lie';
    } else {
        r = 'ok';
    }
    return r;
};


function PassivePlayer() {
    var rand_idx = Math.floor(Math.random() * INITIAL_SET.length);
    this.secret = INITIAL_SET[rand_idx];
}

PassivePlayer.prototype.get_answer = function (question) {
    return evaluate(this.secret, question);
};

window.Solver = Solver;
window.PassivePlayer = PassivePlayer;

//})(); // end solver module


function GUI(control) {
    this.askBtn = document.getElementById('ask');
    this.askedText = document.getElementById('asked_nr');
    this.askTbl = document.getElementById('askTbl');

    this.answerBtn = document.getElementById('answer');
    this.answeredText = document.getElementById('answered');
    this.answerTbl = document.getElementById('answerTbl');
    this.resetBtn = document.getElementById('reset');

    var self = this;
    this.askBtn.addEventListener('click', function () {
        var val = self.askedText.value.replace(' ', '');
        if (/^\d{4}$/.exec(val)) {
            self.askedText.className = '';
            self.askedText.value = '';
            control.on_ask(val);
        } else {
            self.askedText.className = 'invalid';
        }
    });

    this.answerBtn.addEventListener('click', function () {
        var val = self.answeredText.value.replace(' ', '').toLowerCase().replace('o', '0');
        if (/^([x0]{1,4}|-)$/.exec(val)) {
            self.answeredText.className = '';
            self.answeredText.value = '';
            control.on_answer(val);
        } else {
            self.answeredText.className = 'invalid';
        }
    });

    this.askedText.addEventListener('keydown', function (event) {
        if (event.keyCode == 13) {
            self.askBtn.dispatchEvent(new MouseEvent('click'));
        }
    });

    this.answeredText.addEventListener('keydown', function (event) {
        if (event.keyCode == 13) {
            self.answerBtn.dispatchEvent(new MouseEvent('click'));
        }
    });

    this.resetBtn.addEventListener('click', function () {
       control.reset();
    });
}

GUI.prototype.append_ask_line = function (q, a) {
    self.askTbl.insertAdjacentHTML('beforeend', '<tr> <td>' + q + '</td> <td>' + a + '</td> </tr>');
};

GUI.prototype.append_answer_line = function (q, a) {
    self.answerTbl.insertAdjacentHTML('beforeend', '<tr> <td>' + q + '</td> <td>' + a + '</td> </tr>');
};

GUI.prototype.focus_player = function () {
    this.answeredText.disabled = true;
    this.answerBtn.disabled = true;
    this.askedText.disabled = false;
    this.askBtn.disabled = false;
    this.askedText.focus();
};

GUI.prototype.focus_solver = function () {
    this.answeredText.disabled = false;
    this.answerBtn.disabled = false;
    this.askedText.disabled = true;
    this.askBtn.disabled = true;
    this.answeredText.focus();
};

GUI.prototype.reset = function () {
    this.askTbl.innerHTML = '';
    this.answerTbl.innerHTML = '';
    this.answeredText.style.display = '';
    this.answerBtn.style.display = '';
    this.askedText.style.display = '';
    this.askBtn.style.display = '';
};

GUI.prototype.game_end = function () {
    this.answeredText.style.display = 'none';
    this.answerBtn.style.display = 'none';
    this.askedText.style.display = 'none';
    this.askBtn.style.display = 'none';
};

function Control() {
    this.gui = new GUI(this);
    this.reset();
}

Control.prototype.reset = function () {
    this.passive = new PassivePlayer();
    this.solver = new Solver();
    this.gui.focus_player();
    this.gui.reset();
};

function str_mul(s, c) {
    var r = '';
    for (var i = 0; i < c; i++) {
        r += s;
    }
    return r;
}

Control.prototype.on_ask = function (q) {
    var a = this.passive.get_answer(q);
    var x = parseInt(a[0]);
    var z = parseInt(a[1]);
    if (x === 0 && z === 0) {
        a = '-'
    } else {
        a = str_mul('x', x) + str_mul('0', z);
    }
    if (x===4){
        this.gui.append_ask_line('guessed', 'you win');
        this.gui.game_end();
        return;
    }
    this.gui.append_ask_line(q, a);
    this.gui.focus_solver();

    var solver_q = this.solver.get_question();
    this.gui.append_answer_line(solver_q, '');
};

Control.prototype.on_answer = function (answ) {
    var c = 0;
    var nc = 0;

    for (var i = 0; i < answ.length; i++) {
        if (answ[i] == 'x') c += 1;
        if (answ[i] == '0') nc += 1;
    }
    var state = this.solver.send_answer(c, nc);
    var zz = this.gui.answerTbl.getElementsByTagName('td');
    zz[zz.length - 1].innerHTML = '' + answ;
    if (state == 'lie') {
        this.gui.append_answer_line('you lied', 'you loose');
        this.gui.game_end();
    } else if (state == 'success') {
        var solver_q = this.solver.solutions[0];
        this.gui.append_answer_line(solver_q, '');
        this.gui.append_answer_line('guessed', 'I win');
        this.gui.game_end();
    } else {
        this.gui.focus_player();
    }
};


document.addEventListener('DOMContentLoaded', function () {
    control = new Control();
});