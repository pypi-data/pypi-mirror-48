'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const utils_1 = require("../../common/utils");
const cpp = require("child-process-promise");
const cp = require("child_process");
const os = require("os");
const fs = require("fs");
const utils_2 = require("../../common/utils");
const gpuData_1 = require("./gpuData");
const path = require("path");
const typescript_string_operations_1 = require("typescript-string-operations");
async function validateCodeDir(codeDir) {
    let fileCount;
    try {
        fileCount = await utils_1.countFilesRecursively(codeDir);
    }
    catch (error) {
        throw new Error(`Call count file error: ${error}`);
    }
    if (fileCount && fileCount > 1000) {
        const errMessage = `Too many files(${fileCount} found}) in ${codeDir},`
            + ` please check if it's a valid code dir`;
        throw new Error(errMessage);
    }
    return fileCount;
}
exports.validateCodeDir = validateCodeDir;
async function execMkdir(directory) {
    if (process.platform === 'win32') {
        await cpp.exec(`powershell.exe New-Item -Path ${directory} -ItemType "directory" -Force`);
    }
    else {
        await cpp.exec(`mkdir -p ${directory}`);
    }
    return Promise.resolve();
}
exports.execMkdir = execMkdir;
async function execCopydir(source, destination) {
    if (process.platform === 'win32') {
        await cpp.exec(`powershell.exe Copy-Item ${source} -Destination ${destination} -Recurse`);
    }
    else {
        await cpp.exec(`cp -r ${source} ${destination}`);
    }
    return Promise.resolve();
}
exports.execCopydir = execCopydir;
async function execNewFile(filename) {
    if (process.platform === 'win32') {
        await cpp.exec(`powershell.exe New-Item -Path ${filename} -ItemType "file" -Force`);
    }
    else {
        await cpp.exec(`touch ${filename}`);
    }
    return Promise.resolve();
}
exports.execNewFile = execNewFile;
function execScript(filePath) {
    if (process.platform === 'win32') {
        return cp.exec(`powershell.exe -file ${filePath}`);
    }
    else {
        return cp.exec(`bash ${filePath}`);
    }
}
exports.execScript = execScript;
async function execTail(filePath) {
    let cmdresult;
    if (process.platform === 'win32') {
        cmdresult = await cpp.exec(`powershell.exe Get-Content ${filePath} -Tail 1`);
    }
    else {
        cmdresult = await cpp.exec(`tail -n 1 ${filePath}`);
    }
    return Promise.resolve(cmdresult);
}
exports.execTail = execTail;
async function execRemove(directory) {
    if (process.platform === 'win32') {
        await cpp.exec(`powershell.exe Remove-Item ${directory} -Recurse -Force`);
    }
    else {
        await cpp.exec(`rm -rf ${directory}`);
    }
    return Promise.resolve();
}
exports.execRemove = execRemove;
async function execKill(pid) {
    if (process.platform === 'win32') {
        await cpp.exec(`cmd /c taskkill /PID ${pid} /T /F`);
    }
    else {
        await cpp.exec(`pkill -P ${pid}`);
    }
    return Promise.resolve();
}
exports.execKill = execKill;
function setEnvironmentVariable(variable) {
    if (process.platform === 'win32') {
        return `$env:${variable.key}="${variable.value}"`;
    }
    else {
        return `export ${variable.key}=${variable.value}`;
    }
}
exports.setEnvironmentVariable = setEnvironmentVariable;
async function tarAdd(tar_path, source_path) {
    if (process.platform === 'win32') {
        tar_path = tar_path.split('\\').join('\\\\');
        source_path = source_path.split('\\').join('\\\\');
        let script = [];
        script.push(`import os`, `import tarfile`, typescript_string_operations_1.String.Format(`tar = tarfile.open("{0}","w:gz")\r\nfor root,dir,files in os.walk("{1}"):`, tar_path, source_path), `    for file in files:`, `        fullpath = os.path.join(root,file)`, `        tar.add(fullpath, arcname=file)`, `tar.close()`);
        await fs.promises.writeFile(path.join(os.tmpdir(), 'tar.py'), script.join(utils_2.getNewLine()), { encoding: 'utf8', mode: 0o777 });
        const tarScript = path.join(os.tmpdir(), 'tar.py');
        await cpp.exec(`python ${tarScript}`);
    }
    else {
        await cpp.exec(`tar -czf ${tar_path} -C ${source_path} .`);
    }
    return Promise.resolve();
}
exports.tarAdd = tarAdd;
function getScriptName(fileNamePrefix) {
    if (process.platform === 'win32') {
        return fileNamePrefix + '.ps1';
    }
    else {
        return fileNamePrefix + '.sh';
    }
}
exports.getScriptName = getScriptName;
function getgpuMetricsCollectorScriptContent(gpuMetricCollectorScriptFolder) {
    if (process.platform === 'win32') {
        return typescript_string_operations_1.String.Format(gpuData_1.GPU_INFO_COLLECTOR_FORMAT_WINDOWS, gpuMetricCollectorScriptFolder, path.join(gpuMetricCollectorScriptFolder, 'pid'));
    }
    else {
        return typescript_string_operations_1.String.Format(gpuData_1.GPU_INFO_COLLECTOR_FORMAT_LINUX, gpuMetricCollectorScriptFolder, path.join(gpuMetricCollectorScriptFolder, 'pid'));
    }
}
exports.getgpuMetricsCollectorScriptContent = getgpuMetricsCollectorScriptContent;
