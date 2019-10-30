let getColorHex = (color) => {
    let reRGBA = /rgba\((\d+), *(\d+), *(\d+), *([\d.]+)\)/;
    let getHex = (number) => parseInt(number).toString(16).padStart(2, '0');

    let colorOutput = color.match(reRGBA)
    let colorHex = "#";
    colorHex += getHex(colorOutput[1]);
    colorHex += getHex(colorOutput[2]);
    colorHex += getHex(colorOutput[3]);
    colorHex += getHex(Math.round(parseFloat(colorOutput[4]) * 255));
    return colorHex;
}
