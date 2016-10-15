
function GUI(control){
    this.nspitze = document.getElementById('nspitze');
    this.phasediff = document.getElementById('phasediff');
    this.nspitzelbl = document.getElementById('nspitzelbl');
    this.phasedifflbl = document.getElementById('phasedifflbl');
    // this.freq = document.getElementById('freq');
    this.canvas = document.getElementById("canvas");
    this.ctx = canvas.getContext("2d");
    var self = this;
    this.nspitze.addEventListener('change', function () {
        self.nspitzelbl.textContent  = self.nspitze.value;
        control.on_reset(self.nspitze.value, self.phasediff.value, 1);
    });

    this.phasediff.addEventListener('change', function () {
        self.phasedifflbl.textContent  = self.phasediff.value;
        control.on_reset(self.nspitze.value, self.phasediff.value, 1);
    });
    control.on_reset(this.nspitze.value, this.phasediff.value, 1);
};

GUI.prototype.draw = function(time, offset, spokes){
    this.ctx.fillStyle = 'rgba(0,0,0,0.1)';
    this.ctx.strokeStyle = 'rgba(0,153,255,0.8)';

    this.ctx.clearRect(0,0,400,400);
    this.ctx.fillRect(0,0,400,400);
    this.ctx.save();
    this.ctx.translate(200,200);
    this.ctx.beginPath();
    this.ctx.arc(0,0,200,0,Math.PI*2,false);
    this.ctx.stroke();

    for (var i = 0; i < spokes; i++) {
        this.ctx.save();
        this.ctx.rotate(i/spokes*Math.PI);

        this.ctx.beginPath();
        this.ctx.moveTo(-200, 0);
        this.ctx.lineTo(200, 0);
        this.ctx.stroke();

        this.ctx.strokeStyle = 'rgba(255,150,150,0.9)';
        this.ctx.beginPath();

        var x = Math.sin(time+offset*i);

        this.ctx.arc(200*x, 0,8,0,Math.PI*2,false);
        this.ctx.stroke();
        this.ctx.fill();

        this.ctx.restore();
    }
    this.ctx.restore();
};

function Control() {
    this.gui = new GUI(this);
    this.t0time = Date.now();
    var self = this;
    window.setTimeout(function(){self.draw();}, 90)
}

Control.prototype.draw = function(){
    var self = this;
    var time = (Date.now() - this.t0time)/1000;
    this.gui.draw(time, Math.PI*this.phasediff/120, this.nspitze);
    window.setTimeout(function(){self.draw();}, 90)
};

Control.prototype.on_reset = function (nspitze, phasediff, freq) {
    this.nspitze = nspitze;
    this.phasediff = phasediff;
    this.freq = freq;
};

document.addEventListener('DOMContentLoaded', function () {
    control = new Control();
});