# install.packages("meta")
# install.packages("dmetar")
# install.packages("grid")
# install.packages("forestploter")
# install.packages("gridExtra")
# install.packages("ggplot2")

# library(gridExtra)
# library(ggplot2)
# library(dmetar)
library(meta)
# library(grid)
# library(forestploter)


calculateEffectSize = function(params) {
    nt <- params[1,1]
    mt <- params[1,2]
    tdt <- params[1,3]
    nc <- params[1,4]
    mc <- params[1,5]
    tdc <- params[1,6]
    print(tdc)

    m <- metacont(nt, mt, tdt, nc, mc, tdc, sm = "SMD")

    dat <- data.frame(
          label = m[["subgroup.levels"]],
          OR = m[["TE.random.w"]],
          LL = m[["lower.random.w"]],
          UL = m[["upper.random.w"]]
        )

        data_all <- data.frame(
          label = "Effect Size",
          Effect_size = m[["TE"]],
          Standard_Err = m[["seTE"]],
          Pval = m[["pval"]],
          Lower = m[["lower"]],
          Upper = m[["upper"]],
          Weight = m[["w.random"]],
          data = m[["data"]]
        )

        return (data_all)


}
