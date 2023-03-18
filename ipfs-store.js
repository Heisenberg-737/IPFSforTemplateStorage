const Moralis = require("moralis").default;
const fs = require("fs"); 

async function uploadToIpfs() {

    await Moralis.start({
        apiKey: "7hstobdqT97qzSbNkW6Spq227cMCBXEPsKBAM7yk70Wqhiygi3uHD7snLqupcL46",
    });

    const uploadArray = [
        {
            path: "1_tem.json",
            content: fs.readFileSync('/Users/pranay/Projects/Research/ipfs-example/1_tem.json', {encoding: 'base64'})
        },
    ];

    const response = await Moralis.EvmApi.ipfs.uploadFolder({
        abi: uploadArray,
    });

    console.log(response.result)
}

uploadToIpfs();